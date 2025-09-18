from fastapi import APIRouter, Query
from app.routes import metrics  
from app.prompts.baseline import BASELINE_PROMPT
from app.prompts.improved import IMPROVED_PROMPT

router = APIRouter()

@router.post("/")
def classify_text(data: dict, prompt_type: str = Query("baseline", enum=["baseline", "improved"])):
    """
    Classify text using the selected prompt.
    prompt_type: "baseline" or "improved"
    """
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
    
    # Select prompt
    if prompt_type == "baseline":
        prompt_used = BASELINE_PROMPT.format(input=text)
    else:
        prompt_used = IMPROVED_PROMPT.format(input=text)
    
    return {
        "class": classification,
        "confidence": 0.9,
        "prompt_used": prompt_type,  # "baseline" or "improved"
        "latency_ms": latency_ms
    }
