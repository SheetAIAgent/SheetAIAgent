from flask import Flask, jsonify, request
from models.environmental_model import predict_impact

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'energy_usage' not in data:
        return jsonify({"error": "Energy usage not provided"}), 400
    energy_usage = data['energy_usage']
    impact = predict_impact(energy_usage)
    return jsonify({'predicted_impact': impact})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "AI Agent is running successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
