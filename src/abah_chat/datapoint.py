# -------------------------------------------------------------
# This script defines the MyMessageType dataclass, which is used to temporarily store messages exchanged between the user and the LLM agents.
# It includes fields for the message content, the original user input, and a control flag.
# -------------------------------------------------------------

from dataclasses import dataclass
@dataclass
class MyMessageType:
    content : str = ''
    userInput: str = ''
    userPrompt: str = ''
    userFrame: str = ''