import os
import platform
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/info")
def info():
    return jsonify({
        "env":      APP_ENV,
        "hostname": platform.node(),
        "os":       platform.system(),
        "kernel":   platform.release(),
        "time":     datetime.datetime.utcnow().isoformat() + "Z",
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
