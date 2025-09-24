import asyncio
from app.services.pawa_client import PawaClient
from app.agent import SYSTEM_PROMPT

async def main():
    client = PawaClient()
    conversation = [{"role": "system", "content": [{"type": "text", "text": SYSTEM_PROMPT}]}]

    print(" Travel Assistant Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = await client.send_message(SYSTEM_PROMPT, conversation, user_input)
        reply = response.get("reply", "No reply.")

        print(f"Agent: {reply}\n")

        conversation.append({"role": "user", "content": [{"type": "text", "text": user_input}]})
        conversation.append({"role": "assistant", "content": [{"type": "text", "text": reply}]})

if __name__ == "__main__":
    asyncio.run(main())
