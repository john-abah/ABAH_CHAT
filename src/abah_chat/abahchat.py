from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core import (
    RoutedAgent, message_handler, MessageContext, AgentId)
from autogen_core import (
    RoutedAgent, message_handler, MessageContext, AgentId)
from .datapoint import MyMessageType
import os
import json
from .agentFunctions import add_json, fileCreation
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Color definitions
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
class chatter(RoutedAgent):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        model_info = {"type": "ollama_chat", 
                      "model": "gemma4:12b", 
                      "json_output": True,
                      "vision": True,
                      "function_calling": False}
        # Keep an identifier for this classifier instance.
        self.chatterId = AgentId("chatter", self.id.key)
        # Configure the local Ollama vision model with deterministic generation.
        self.model_client = OllamaChatCompletionClient(model="gemma4:12b", model_info=model_info, options={"num_ctx": 4096, "stream":False, "temperature":0})
        # Delegate image classification while retaining only a short conversation context.
        self._delegate = AssistantAgent(name, model_client=self.model_client,
                                        system_message="""### SYSTEM ROLE
                                        You are a personal loyal companion. You answer as briefly and as concisely as possible""")
    @message_handler
    async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
        # Announce the search-based coding workflow to the user.
        await fileCreation()
        count =0
        while True:
            if count>=1:
                print("\n")
                message.content= input(f"{RED}<< {RESET}")
            json_file = f"{BASE_DIR}/memory.json"
            with open(json_file, "r+", encoding="utf-8") as file:
                    data = json.load(file)
                    agent_state = data
            await self._delegate.load_state(agent_state)
            print(f"\n{self.id.type} {RED}>>")
            query = [TextMessage(content=message.content, source="user")]
            response = await self._delegate.on_messages(
            query, ctx.cancellation_token
        )
            print(f"\n{BLUE}{response.chat_message.content}{RESET}")

            agent_state=await self._delegate.save_state()
            await add_json(agent_state)
            count+=1
        await self.model_client.close()