from app import storage

def update_classification_metrics(classification: str, latency_ms: float):
    storage.metrics_data["classification"]["total_requests"] += 1
    if classification in storage.metrics_data["classification"]["class_distribution"]:
        storage.metrics_data["classification"]["class_distribution"][classification] += 1
    
    # Track latencies for average calculation
    storage.metrics_data["classification"].setdefault("latencies", []).append(latency_ms)
    
    # Update average latency
    latencies = storage.metrics_data["classification"]["latencies"]
    storage.metrics_data["classification"]["average_latency_ms"] = sum(latencies) / len(latencies)

def update_feedback_metrics(predicted: str, correct: str):
    storage.metrics_data["feedback"]["total_feedback"] += 1
    if predicted == correct:
        storage.metrics_data["feedback"]["correct_count"] += 1
    else:
        storage.metrics_data["feedback"]["incorrect_count"] += 1

def get_classification_metrics():
    return {
        "total_requests": storage.metrics_data["classification"]["total_requests"],
        "class_distribution": storage.metrics_data["classification"]["class_distribution"],
        "average_latency_ms": storage.metrics_data["classification"].get("average_latency_ms", 0.0)
    }

def get_feedback_metrics():
    return storage.metrics_data["feedback"]
