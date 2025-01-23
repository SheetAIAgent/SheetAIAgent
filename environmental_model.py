import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Train data (Energy consumption vs Environmental impact)
X = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
y = np.array([50, 40, 30, 20, 10])

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a file
with open('models/ai_impact_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Function to predict environmental impact based on energy usage
def predict_impact(energy_usage):
    model = pickle.load(open('models/ai_impact_model.pkl', 'rb'))
    prediction = model.predict([[energy_usage]])
    return prediction[0]

# Predict impact for a given energy usage
energy_usage = 60
predicted_impact = predict_impact(energy_usage)
print(f"Predicted environmental impact for {energy_usage} kWh usage: {predicted_impact}")
