# Simple in-memory storage for metrics and feedback
metrics_data = {
    "classification": {
        "total_requests": 0,
        "class_distribution": {
            "toxic": 0,
            "spam": 0,
            "safe": 0
        },
        "latencies": []
    },
    "feedback": {
        "total_feedback": 0,
        "correct_count": 0,
        "incorrect_count": 0
    }
}