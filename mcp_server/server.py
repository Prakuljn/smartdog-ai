from flask import Flask, request, jsonify

app = Flask(__name__)
latest_alert = {}

@app.route("/report", methods=["POST"])
def new_report():
    global latest_alert
    latest_alert = request.json
    return {"status": "received"}, 200

@app.route("/report/latest", methods=["GET"])
def get_latest():
    return jsonify(latest_alert)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
