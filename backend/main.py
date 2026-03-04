from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import re

app = FastAPI(title="Digital Twin Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ANONYMIZED MOCK DATA STORE ---
TWIN_STATE = {
    "profile": {
        "name": "Lakshya Asnani",
        "university": "Vellore Institute of technology",
        "status": "Active"
    },
    "metrics": {
        "coding_streak_days": 14,
        "focus_score": 65,            
        "current_stress_score": 8.5,  # High stress trigger
        "sleep_deficit_hours": 5.0
    },
    "goals": [
        {"name": "Master Dynamic Programming", "progress": 60},
        {"name": "Maintain 8 Hours Sleep", "progress": 45}
    ],
    "agent_status": {
        "needs_intervention": True,
        "agent_message": "Critical sleep deficit detected. Cognitive load is high. I have autonomously rescheduled tonight's algorithm practice to tomorrow.",
        "history": [
            {"time": "10:00 AM", "action": "Detected skipped breakfast. Flagged energy dip risk."},
            {"time": "02:30 PM", "action": "Noticed 3 hours of continuous study. Suggested 15m screen break."}
        ]
    },
    "schedule": [
        {"id": 1, "time": "09:00 AM", "task": "Operating Systems Lecture", "type": "Academic", "status": "completed"},
        {"id": 2, "time": "02:00 PM", "task": "Capstone Project Work", "type": "Project", "status": "pending"},
        {"id": 3, "time": "08:00 PM", "task": "Advanced Algorithmic Practice", "type": "Coding", "status": "agent_blocked"}, 
        {"id": 4, "time": "08:30 PM", "task": "Mandatory Recovery Time", "type": "Well-being", "status": "agent_added"}
    ]
}

class JournalData(BaseModel):
    text: str

@app.get("/api/twin/state")
def get_state():
    return TWIN_STATE

@app.post("/api/twin/sync_apis")
def sync_apis():
    """Simulates pulling data from GitHub and LeetCode"""
    timestamp = datetime.now().strftime("%I:%M %p")
    TWIN_STATE["metrics"]["coding_streak_days"] += 1
    TWIN_STATE["goals"][0]["progress"] = min(100, TWIN_STATE["goals"][0]["progress"] + 2)
    TWIN_STATE["agent_status"]["history"].insert(0, {"time": timestamp, "action": "API Sync: Pulled 3 commits from GitHub, 1 LeetCode submission."})
    return {"message": "APIs Synced", "new_state": TWIN_STATE}

@app.post("/api/twin/journal")
def process_journal(data: JournalData):
    """Simulates NLP Entity Extraction from a journal entry"""
    timestamp = datetime.now().strftime("%I:%M %p")
    text = data.text.lower()
    
    extracted_actions = []

    # Simulate extracting sleep data
    sleep_match = re.search(r'slept.*?(\d+)|sleep.*?(\d+)', text)
    if sleep_match:
        hours = float(sleep_match.group(1) or sleep_match.group(2))
        TWIN_STATE["metrics"]["sleep_deficit_hours"] = max(0, TWIN_STATE["metrics"]["sleep_deficit_hours"] - hours)
        TWIN_STATE["goals"][1]["progress"] = min(100, TWIN_STATE["goals"][1]["progress"] + (hours * 5))
        extracted_actions.append(f"Extracted sleep: {hours}h")
        
        # Heal state if sleep is good
        if TWIN_STATE["metrics"]["sleep_deficit_hours"] < 2:
            TWIN_STATE["metrics"]["current_stress_score"] = 4.0
            TWIN_STATE["agent_status"]["needs_intervention"] = False
            TWIN_STATE["agent_status"]["agent_message"] = "Metrics stabilized. Schedule optimized for peak productivity."
            TWIN_STATE["schedule"][2]["status"] = "pending" # Unblock task

    # Simulate extracting coding data
    if "leetcode" in text or "code" in text or "github" in text:
        TWIN_STATE["metrics"]["coding_streak_days"] += 1
        TWIN_STATE["metrics"]["current_stress_score"] += 0.5
        extracted_actions.append("Extracted coding activity")

    # Simulate extracting stress
    if "stress" in text or "tired" in text or "exhausted" in text:
        TWIN_STATE["metrics"]["current_stress_score"] = min(10.0, TWIN_STATE["metrics"]["current_stress_score"] + 2.0)
        extracted_actions.append("Extracted high stress indicator")

    action_text = "NLP Processed: " + ", ".join(extracted_actions) if extracted_actions else "NLP Processed: No actionable metrics found."
    TWIN_STATE["agent_status"]["history"].insert(0, {"time": timestamp, "action": action_text})

    return {"message": "Journal Processed", "new_state": TWIN_STATE}