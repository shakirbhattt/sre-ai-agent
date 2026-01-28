def detect_incident(metrics):
    if metrics["error_rate"] > 5 and metrics["latency_p95"] > 1:
        return {
            "incident": True,
            "severity": "HIGH",
            "reason": "High error rate and latency breach"
        }
    return {
        "incident": False
    }
