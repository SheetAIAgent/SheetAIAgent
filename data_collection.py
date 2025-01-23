import requests
import pandas as pd
from datetime import datetime

# Function to fetch real-time energy usage data from an API
def fetch_energy_usage():
    # Example API endpoint
    api_url = "https://api.energyusage.com/data"
    response = requests.get(api_url)
    data = response.json()
    return data

# Save the data in a CSV file for later analysis
def save_data_to_csv(data, filename='energy_usage_data.csv'):
    df = pd.DataFrame(data)
    df['timestamp'] = datetime.now()
    df.to_csv(filename, index=False)

# Fetch and save data
energy_data = fetch_energy_usage()
save_data_to_csv(energy_data)
print(f"Data saved successfully at {datetime.now()}")
