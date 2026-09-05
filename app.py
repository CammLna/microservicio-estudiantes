from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "service": "Microservicio DevOps", "version": "1.0.0"}), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/api/v1/info", methods=["GET"])
def info():
    return jsonify({"proyecto": "Evaluacion Parcial 1 DevOps", "integrantes": 3, "estado": "en desarrollo"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
