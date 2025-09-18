from fastapi import APIRouter
from app.routes import metrics  # Import the metrics module
from app.prompts.baseline import BASELINE_PROMPT
from app.prompts.improved import IMPROVED_PROMPT

router = APIRouter()

@router.post("/")
def classify_text(data: dict):
    text = data.get("text")
    
    # Dummy classification logic
    if "hate" in text.lower():
        classification = "toxic"
    elif "win money" in text.lower():
        classification = "spam"
    else:
        classification = "safe"

    latency_ms = 50  # Dummy latency
    
    # Update classification metrics
    metrics.update_classification_metrics(classification, latency_ms)
    
    # Choose which prompt was used
    prompt_used = BASELINE_PROMPT.format(input=text)  # or IMPROVED_PROMPT
    
    return {
        "class": classification,
        "confidence": 0.9,
        "prompt_used": "baseline",  # change to "improved" if using improved prompt
        "latency_ms": latency_ms
    }
