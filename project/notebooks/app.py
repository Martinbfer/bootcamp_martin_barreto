from flask import Flask, request, jsonify
import pickle
import numpy as np

# load model once
with open("model/ko_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "KO API running"})

@app.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        # accept either query params (GET) or JSON (POST)
        if request.method == "GET":
            lag1 = float(request.args.get("lag1"))
            vol = float(request.args.get("volatility_21d"))
        else:
            data = request.get_json(force=True)
            lag1 = float(data["lag1"])
            vol = float(data["volatility_21d"])

        X = np.array([[lag1, vol]])
        pred = int(model.predict(X)[0])  # 1 = up, 0 = down
        return jsonify({"prediction": pred, "inputs": {"lag1": lag1, "volatility_21d": vol}})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/plot", methods=["GET"])
def plot():
    import matplotlib.pyplot as plt
    import io
    from flask import send_file
    fig, ax = plt.subplots()
    ax.plot([0,1,2,3],[0,1,4,9])
    ax.set_title("Demo Plot")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=120)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
