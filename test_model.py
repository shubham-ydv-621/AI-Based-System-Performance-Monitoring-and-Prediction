import pickle
import pandas as pd  # Import pandas to create a DataFrame

# Load the trained AI model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Example input data for prediction (replace with actual system stats or any values)
memory = 50  # Example memory usage in percentage
disk = 40    # Example disk usage in percentage

# Convert input data to a DataFrame with the correct feature names
input_data = pd.DataFrame([[memory, disk]], columns=['Memory', 'Disk'])

# Get the prediction for CPU usage based on memory and disk usage
prediction = model.predict(input_data)

print(f"Predicted CPU Usage: {prediction[0]}%")
