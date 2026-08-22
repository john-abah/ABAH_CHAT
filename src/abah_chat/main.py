# -------------------------------------------------------------
# This script implements the scheduling algorithm for the LLM agents, using the Autogen Framework.
# It initializes the coder and verificator agents, and handles user input to trigger the coding and verification process.
# -------------------------------------------------------------

# Import the agent classes and runtime utilities needed to run the workflow.
from .datapoint import MyMessageType
from .abahchat import chatter
from autogen_core import (AgentId, SingleThreadedAgentRuntime)
import asyncio
import os
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
async def main():
    try:
        runtime = SingleThreadedAgentRuntime()

        # Register the coder and verificator agents with the runtime.
        await chatter.register(runtime, "chatter", lambda: chatter('chatter'))
        runtime.start() 
        # Prompt the user for the task text and send it to the coder agent.
        input_text = input(f"\n\n{BLUE}What's on your mind?{RESET} ")
        print("\n\n")
        await runtime.send_message(MyMessageType(content=input_text), AgentId("chatter", "chatter"))
    except asyncio.exceptions.CancelledError:
        print(f"\n\nThe process has been terminated. Good bye\n\n")
    except RuntimeError:
        print(f"\n\nThe process has been terminated. Good bye\n\n")
    except KeyboardInterrupt:
        # Stop the runtime cleanly if the user interrupts the program.
        print(f"\n\nThe process has been terminated. Good bye\n\n")
    finally:
        print("Exiting...\n")
        os._exit(0)
def ABAH_CHAT():
   asyncio.run(main())