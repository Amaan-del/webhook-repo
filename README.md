# Webhook Receiver App (Flask + MongoDB + GitHub Webhooks)

This app listens for GitHub webhook events (`push`, `pull_request`, and `merge`) and stores them in MongoDB. A clean UI polls the latest activity every 15 seconds.

---

## 🔧 Features

- Receives GitHub webhook events via `/webhook`
- Parses event data (author, branches, timestamp)
- Saves formatted message in MongoDB
- Frontend UI polls and displays latest activity

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/webhook-repo.git
cd webhook-repo
Install dependencies
pip install -r requirements.txt
Run Flask app
python app.py
