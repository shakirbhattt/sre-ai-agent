# 🤖 SRE AI Agent

This project is a **simple SRE AI Agent** designed for beginners to understand **Site Reliability Engineering (SRE)**, **incident detection**, and **AIOps fundamentals**.

The agent runs as a **single Python file** and simulates how SRE teams detect incidents, assess severity, and suggest remediation actions.

---

## 🎯 Project Goal

To demonstrate how an SRE-style system:
- Collects service metrics
- Detects incidents using simple rules
- Explains what went wrong
- Suggests safe remediation steps

This project focuses on **thinking like an SRE**, not complex tooling.

---

## 🧠 What This Agent Does

- Simulates metrics such as latency, error rate, CPU, and traffic
- Detects incidents based on SRE thresholds
- Classifies severity
- Provides remediation suggestions
- Runs in recommendation-only mode (no auto-fix)

---

## 🏗️ Architecture (Simplified)

Metrics → Incident Detection → Decision Logic → Human-Readable Output

---

## ⚙️ Prerequisites

- Python 3.8 or higher
- Basic understanding of command line
- Git (optional)

Check Python version:

python3 --version

---

## 🚀 How to Run

Clone the repository:


git clone https://github.com/your-username/sre-ai-agent.git

cd sre-ai-agent

---

## 🏃 Run the SRE AI Agent:

python sre_ai_agent.py

---

Example Output

📊 Metrics Collected:
- latency_p95: 1.8s
- error_rate: 12%
- cpu: 40%
- traffic_rpm: 1200

🚨 INCIDENT DETECTED
Severity: HIGH
Reason: High error rate and latency breach

Suggested Actions:
- Rollback last deployment
- Check downstream dependencies
- Scale service temporarily
