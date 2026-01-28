from metrics import get_metrics
from detector import detect_incident

def run_agent():
    metrics = get_metrics()
    result = detect_incident(metrics)

    print("📊 Metrics:", metrics)

    if result["incident"]:
        print("🚨 INCIDENT DETECTED")
        print("Severity:", result["severity"])
        print("Reason:", result["reason"])
        print("Suggested Actions:")
        print("- Rollback last deployment")
        print("- Check downstream dependencies")
        print("- Scale service temporarily")
    else:
        print("✅ System healthy")

if __name__ == "__main__":
    run_agent()
