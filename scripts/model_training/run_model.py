from training_and_baseline import random_output, load_models
from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Currently I'm allowing everything

vectorizer, model = load_models()

# print(random_output("I love donald trump", vectorizer, model))


def convert_to_serializable(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert_to_serializable(item) for item in obj]
    return obj


@app.route("/api/analyze", methods=["POST"])
def analyze_text():
    try:
        data = request.get_json()  # Getting the json data
        text = data.get("text")

        if not text:
            return jsonify({"error", "Incorrect/No text provided"}), 400

        output_text = random_output(
            text, vectorizer, model
        )  # Outputs <class 'numpy.int64'>

        processed_output = convert_to_serializable(output_text)

        result = {"original_text": text, "output": processed_output}

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
