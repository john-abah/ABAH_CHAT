import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
async def extract_json(code):
    pass
async def add_json(new_json):
    # Load the existing scene data before adding a scenic result.
    json_file = f"{BASE_DIR}/memory.json"
    with open(json_file, "r+", encoding="utf-8") as file:
        data = json.load(file)
        for message in new_json["llm_context"]["messages"]:
            data["llm_context"]["messages"].append(message)
        file.seek(0)
        json.dump(data, file, indent=4)

async def fileCreation():
    json_file = os.path.join(BASE_DIR, "memory.json")
    if os.path.isfile(json_file)==False:
        print("Generating File...\n")
        agent_state={'type': 'AssistantAgentState', 'version': '1.0.0', 'llm_context': {'messages': [{'content': '', 'source': 'user', 'type': 'UserMessage'}, {'content': '', 'thought': None, 'source': 'chatter', 'type': 'AssistantMessage'}]}}
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(agent_state, f, indent=4)
        print("Done...\n")
    else:
        print("Using available memory file\n")
    