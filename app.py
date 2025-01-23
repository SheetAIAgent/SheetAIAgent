from flask import Flask, request, jsonify
from ai_model_demo import predict_impact

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    energy_usage = data['energy_usage']
    impact = predict_impact(energy_usage)
    return jsonify({'predicted_impact': impact})

if __name__ == '__main__':
    app.run(debug=True)
