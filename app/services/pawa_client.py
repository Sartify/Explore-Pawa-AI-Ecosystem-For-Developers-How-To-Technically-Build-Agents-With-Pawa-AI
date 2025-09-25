import os
import json
import requests
from dotenv import load_dotenv

from app.services.tools import search_buses, book_bus

load_dotenv()

PAWA_API_KEY = os.getenv("PAWA_API_KEY")
PAWA_API_URL = os.getenv("PAWA_API_URL", "https://staging.api.pawa-ai.com/v1/chat/request")
MODEL_NAME = os.getenv("MODEL_NAME", "pawa-v1-blaze-20240924")


class PawaClient:
    """Handles communication with Pawa AI chat model"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or PAWA_API_KEY
        self.url = PAWA_API_URL
        self.model = MODEL_NAME

    async def send_message(self, system_prompt: str, conversation: list, user_input: str) -> dict:
        """Send message to Pawa API, handle tool calls if needed."""

        payload = {
            "model": self.model,
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 4096,
            "frequency_penalty": 0.3,
            "presence_penalty": 0.3,
            "seed": 2024,
            "stream": False,
            "tool_choice": "auto",
            "messages": conversation + [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_input}
                    ],
                }
            ],
            "tools": [
                {
                    "function": {
                        "name": "search_buses",
                        "description": "Search available buses for a route.",
                        "strict": True,
                        "parameters": {
                            "additionalProperties": False,
                            "type": "object",
                            "properties": {
                                "from": {"type": "string", "description": "Departure city"},
                                "to": {"type": "string", "description": "Destination city"},
                            },
                            "required": ["from", "to"],
                        },
                    },
                    "type": "function",
                },
                {
                    "function": {
                        "name": "book_bus",
                        "description": "Book a bus seat by ID.",
                        "strict": True,
                        "parameters": {
                            "additionalProperties": False,
                            "type": "object",
                            "properties": {
                                "bus_id": {"type": "string", "description": "ID of the bus"},
                                "name": {"type": "string", "description": "Passenger name"},
                                "phone": {"type": "string", "description": "Contact phone number"},
                            },
                            "required": ["bus_id", "name", "phone"],
                        },
                    },
                    "type": "function",
                },
                {
                    "function": {
                        "name": "cancel_booking",
                        "description": "Cancel a bus booking by booking ID.",
                        "strict": True,
                        "parameters": {
                            "additionalProperties": False,
                            "type": "object",
                            "properties": {
                                "booking_id": {"type": "string", "description": "Booking reference ID"},
                            },
                            "required": ["booking_id"],
                        },
                    },
                    "type": "function",
                },
            ],
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        response = requests.post(self.url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        resp_json = response.json()
        # print("Pawa Response:", json.dumps(resp_json, indent=2))  # Debug

        # Extract assistant response
        request_list = resp_json.get("data", {}).get("request", [])
        if not request_list:
            return {"reply": "No response from AI."}

        assistant_message = request_list[0].get("message", {})
        # print("Assistant Message:", json.dumps(assistant_message, indent=2))  # Debug
        tool_calls = assistant_message.get("tool_calls", [])
        # print("Tool Calls:", json.dumps(tool_calls, indent=2))  # Debug

        # Handle tool calls
        if tool_calls:
            for call in tool_calls:
                func = call.get("function", {})
                args_str = func.get("arguments", "{}")
                args = json.loads(args_str)

                if func.get("name") == "search_buses":
                    return {"reply": search_buses(args)}

                if func.get("name") == "book_bus":
                    return {"reply": book_bus(args)}

        # Handle normal text
        reply_text = assistant_message.get("content", "")
        if isinstance(reply_text, list):
            reply_text = " ".join(
                [c.get("text", "") for c in reply_text if "text" in c]
            )

        return {"reply": reply_text.strip()}
