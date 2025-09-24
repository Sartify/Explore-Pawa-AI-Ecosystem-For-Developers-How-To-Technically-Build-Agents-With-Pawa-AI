
---

#  Travel Assistant Agent

##  Overview

**Travel Assistant Agent** is an AI-powered demo project that showcases how **intelligent agents** can assist users in planning and booking bus tickets.
Unlike a simple chatbot, this agent can **reason**, **use tools**, and **take actions** such as searching bus schedules, booking seats, and cancelling bookings.

The project was built as part of a **conference demo** to illustrate the power of **AI Agents with Pawa AI models** in real-world applications.

---

##  Features

*  **Natural Conversation** – chat with the agent in plain language.
*  **Bus Search Tool** – find available buses between two cities.
*  **Booking Tool** – simulate booking a bus seat with passenger details.
*  **Cancellation Tool** – cancel a booking using booking ID.
*  **Context Awareness** – remembers conversation flow for natural interaction.
*  **Future Ready** – can be integrated with real APIs like **TGO** or bus company systems.

---

##  Architecture

The agent is built around **three core components**:

1. **Model (Pawa AI)**

   * Powers the natural language understanding and reasoning.
   * Responds based on system instructions and conversation history.

2. **Tools (Custom Functions)**

   * `search_buses`: search available buses between two cities.
   * `book_bus`: book a bus seat by bus ID and passenger name.
   * `cancel_booking`: cancel an existing booking.

3. **Knowledge & Memory**

   * The agent maintains conversation history to provide contextual responses.

---

##  Project Structure

```bash
.
├── app/
│   ├── run.py               # Entry point to run the agent
│   ├── services/
│   │   ├── pawa_client.py   # Handles API requests to Pawa AI
│   │   └── tools.py         # Implements search, booking, and cancellation tools
│   └── agent.py            # System prompt and configuration
├── env/                     # Virtual environment (not included in repo)
├── .env                     # Environment variables (API key, model name, etc.)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/travel-assistant-agent.git
cd travel-assistant-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv env
source env/bin/activate   # Linux / Mac
env\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file in the root directory:

```ini
PAWA_API_KEY=your_api_key_here
PAWA_API_URL=https://staging.api.pawa-ai.com/v1/chat/request
MODEL_NAME=pawa-v1-ember-20240924
```

---

##  Usage

Run the agent from terminal:

```bash
python -m app.run
```

You’ll see:

```
Travel Assistant Agent (type 'exit' to quit)

You: hello
Agent: Hello! I am your Travel Assistant Agent. How can I help you today?
```

### Example Interactions

```
You: I want to travel from Dar es Salaam to Mwanza
Agent: Available buses from Dar es Salaam to Mwanza:
- Shabiby (B001): 08:00 AM @ 45,000 TZS
- Kiliman (B002): 09:30 AM @ 47,000 TZS

You: Book Shabiby for John
Agent: Booking confirmed!
Passenger: John
Bus: Shabiby (B001)
From: Dar es Salaam To: Mwanza
Time: 08:00 AM
Seat No: 12
Price: 45,000 TZS
```

---

##  Future Improvements

* Integrate with **real-time APIs** (TGO, Shabiby, BM Luxury, etc.).
* Add **payments** (e.g., Mobile Money, Card).
* Extend to **air travel and trains**.
* Build a **web or mobile UI** for user-friendly booking.
* Add **multimodal support** (voice queries, SMS, WhatsApp).

---

##  Acknowledgements

* **Pawa AI** for providing the model API.
* Inspiration from real-world bus booking systems in Tanzania.
* Conference organizers and participants for the motivation to build this demo.

---

 With this project, we show that AI Agents are not just for answering questions—they can **act, assist, and simplify real-life tasks** like booking your next bus journey.

---
