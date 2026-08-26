from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>CloudOps</h1>
    <h2>System Status: Operational</h2>
    <p>Environment: Production</p>
    <p>Version: 1.0.0</p>
    """


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        service="cloudops"
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
