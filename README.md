# ✈️ Agentic Travel Assistant

An AI-powered multi-agent travel assistant built with LangGraph that automates travel planning by orchestrating specialized agents for flight discovery, hotel recommendations, itinerary generation, and final travel response creation.

Designed as an end-to-end agentic workflow with persistent memory, external tool integration, and an interactive Streamlit interface.

---

## Features

- Multi-agent orchestration using LangGraph
- Flight information retrieval
- Hotel recommendations through web search
- AI-generated travel itineraries
- Persistent conversation memory using PostgreSQL
- Interactive Streamlit interface
- Modular architecture for extensibility
- Session-based execution support

---

## Architecture

```text
User Query
     │
     ▼
┌──────────────┐
│ Flight Agent │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Hotel Agent  │
└──────┬───────┘
       │
       ▼
┌─────────────────┐
│ Itinerary Agent │
└──────┬──────────┘
       │
       ▼
┌─────────────┐
│ Final Agent │
└──────┬──────┘
       │
       ▼
Final Travel Plan
```

---

## Tech Stack

### AI & Orchestration
- LangGraph
- LangChain
- Groq (Llama 3.3 70B)

### Backend
- Python
- PostgreSQL

### Search & Retrieval
- Tavily Search API
- AviationStack API

### Frontend
- Streamlit

### Infrastructure
- LangGraph Checkpointing

---

## Project Structure

```bash
Agentic-Travel-Assistant-LangGraph/

├── agents/
│   ├── flight.py
│   ├── hotel.py
│   ├── itinerary.py
│   └── final.py

├── config/
│   └── llm.py

├── graph/
│   └── workflow.py

├── memory/
│   └── checkpoint.py

├── schemas/
│   └── state.py

├── tools/
│   ├── flight_tool.py
│   └── search_tool.py

├── frontend.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Workflow

### Flight Agent
Collects flight information through AviationStack.

↓

### Hotel Agent
Retrieves hotel recommendations using Tavily.

↓

### Itinerary Agent
Combines flight and hotel data to generate a personalized travel plan.

↓

### Final Agent
Creates a final user-facing response.

---

## Installation

### Clone

```bash
git clone <repo-url>

cd Agentic-Travel-Assistant-LangGraph
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create:

```bash
.env
```

Add:

```env
GROQ_API_KEY=

DATABASE_URL=

TAVILY_API_KEY=

AVIATIONSTACK_API_KEY=
```

---

## Run Application

CLI:

```bash
python main.py
```

Streamlit:

```bash
streamlit run frontend.py
```

---

## Example Query

```text
Plan a 5 day trip to Istanbul under $1500
```

Example Output:

```text
Flights
Hotels
Day-wise itinerary
Recommendations
```

---

## Current Capabilities

✓ Multi-agent execution

✓ Persistent memory

✓ External tool integration

✓ Interactive UI

---

## Future Improvements

- Dynamic routing
- Human-in-the-loop approvals
- FastAPI API layer
- Docker deployment
- Cost tracking
- Tool retries
- Streaming responses
- Multi-user sessions

---


## License

MIT
