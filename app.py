from flask import Flask, request, jsonify, render_template
from db import events_collection
from utils import format_event
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    event_type = request.headers.get("X-GitHub-Event")
    data = request.get_json()

    formatted = format_event(event_type, data)
    if formatted:
        events_collection.insert_one({
            "message": formatted,
            "timestamp": datetime.utcnow()
        })

    return jsonify({"status": "received"}), 200

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events", methods=["GET"])
def get_events():
    events = events_collection.find().sort("timestamp", -1).limit(10)
    return jsonify([e["message"] for e in events])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
