#  Personal Digital Twin Agent 

> **An AI-driven Digital Twin for Undergraduate Academic & Well-Being Management.**

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

##  Project Overview
While "Digital Twins" are traditionally used in industrial IoT and smart cities, this project applies the concept to human productivity. This application creates a real-time, digitized state of an undergraduate student—tracking academic workload, coding habits, and physical well-being (sleep/stress). 

Moving beyond standard "to-do apps," this system acts as an **Agentic AI**. It features memory, goal-tracking, and autonomous action planning (e.g., dynamically replanning a schedule to prevent burnout if a severe sleep deficit is detected).

##  Key Features
* ** Dynamic State Representation:** Calculates real-time metrics like *Burnout Risk*, *Coding Streaks*, and *Sleep Deficits* based on continuous data ingestion.
* ** Agentic Schedule Intervention:** Autonomously blocks or adds events to the user's timeline (e.g., forcing "Recovery Time") when critical health thresholds are breached.
* ** Digital Exhaust Sync:** Ingests skill metrics passively by polling external APIs (Simulating GitHub commits and LeetCode problem-solving streaks).
* ** NLP Daily Check-in:** Replaces manual forms with Natural Language Processing. Users journal their day, and the AI extracts key metrics (hours slept, stress levels, tasks completed) to update the Twin's state.

##  System Architecture 
The pipeline operates on a continuous feedback loop:
1. **Sensors (Ingestion):** API Polling & NLP Journal Extraction.
2. **State Store (Memory):** Synthesizes raw data into a quantified "Twin State" (Current Phase: In-Memory Python Dictionary $\rightarrow$ Future: PostgreSQL).
3. **Intelligence Engine:** Evaluates the state against user goals and health thresholds.
4. **Action (Frontend):** React dashboard visualizes the Twin and executes Agentic schedule overrides.

##  Getting Started (Local Development)

### Prerequisites
* Node.js & npm (for frontend)
* Python 3.8+ (for backend)

### 1. Clone the Repository
git clone [https://github.com/your-username/digital-twin-agent.git](https://github.com/your-username/digital-twin-agent.git)
cd digital-twin-agent
### 2. Run the FastAPI Backend
Bash
cd backend
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
The API will be available at http://localhost:8000

### 3. Run the React Frontend
Bash
cd frontend
npm install
npm run dev # or npm start, depending on your setup
The dashboard will be available at http://localhost:3000 or http://localhost:5173

### Development Roadmap
This repository is currently in the High-Fidelity Proof of Concept (v1.0) phase.

[x] Phase 1: Architecture & UI Shell (FastAPI routing, React Dashboard, Rule-based Agent logic).

[ ] Phase 2: Automated Data Ingestion (Real OAuth integration with GitHub and LeetCode APIs).

[ ] Phase 3: LLM Integration (Integrating LangChain/Gemini to replace rule-based logic with true generative reasoning for interventions).

[ ] Phase 4: State Persistence (Migrating from in-memory state to PostgreSQL via SQLAlchemy).

[ ] Phase 5: Calendar Sync (Bi-directional syncing with Google Calendar API).

📄 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
