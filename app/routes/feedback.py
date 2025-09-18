from fastapi import APIRouter
from app import storage

router = APIRouter()

@router.post("/")
def submit_feedback(data: dict):
    text = data.get("text")
    predicted = data.get("predicted")
    correct = data.get("correct")
    prompt_used = data.get("prompt_used", "baseline")  # optional field
    
    # Store feedback in memory
    storage.metrics_data["feedback"]["total_feedback"] += 1
    if predicted == correct:
        storage.metrics_data["feedback"]["correct_count"] += 1
    else:
        storage.metrics_data["feedback"]["incorrect_count"] += 1

    # Optional: store prompt usage in each feedback entry
    storage.metrics_data.setdefault("feedback_entries", []).append({
        "text": text,
        "predicted": predicted,
        "correct": correct,
        "prompt_used": prompt_used
    })

    return {
        "status": "received",
        "data": {
            "text": text,
            "predicted": predicted,
            "correct": correct,
            "prompt_used": prompt_used
        }
    }
