import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data for energy usage and environmental impact
energy_usage = np.array([10, 20, 30, 40, 50])
impact = np.array([50, 40, 30, 20, 10])

# Fit linear regression model
model = LinearRegression()
model.fit(energy_usage.reshape(-1, 1), impact)

# Predict environmental impact for different energy usages
predicted_impact = model.predict(energy_usage.reshape(-1, 1))

# Plot the results
plt.scatter(energy_usage, impact, color='blue', label='Actual Data')
plt.plot(energy_usage, predicted_impact, color='red', label='Predicted Model')
plt.title('Energy Usage vs Environmental Impact')
plt.xlabel('Energy Usage (kWh)')
plt.ylabel('Environmental Impact (Impact Score)')
plt.legend()
plt.show()

# Save the model for future predictions
import pickle
with open('environmental_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training completed and saved as 'environmental_model.pkl'")
