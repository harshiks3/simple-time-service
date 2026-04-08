from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.headers.get("X-Forwarded-For", request.remote_addr)
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)