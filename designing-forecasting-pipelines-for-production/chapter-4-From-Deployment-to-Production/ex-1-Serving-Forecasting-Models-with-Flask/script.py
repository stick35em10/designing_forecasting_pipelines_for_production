import warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

import pandas as pd
from flask import Flask, request, jsonify

# Load the trained MLflow model
import mlflow.pyfunc
logged_model = 'runs:/your_run_id/your_model_path'  # Replace with actual run ID and model path
loaded_model = mlflow.pyfunc.load_model(logged_model)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        json_ = request.json
        logger.info(f"Incoming request: {json_}")

        # Assuming the incoming JSON is a dictionary where keys are feature names
        # and values are the feature values.
        # It needs to be converted to a pandas DataFrame for the model.
        data = pd.DataFrame([json_])

        # Make prediction
        prediction = loaded_model.predict(data)

        # Assuming the prediction is a single value
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)