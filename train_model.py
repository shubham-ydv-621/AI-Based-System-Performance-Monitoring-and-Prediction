import psutil
import time
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Collect data for training the model (for 10 minutes)
data = []
for _ in range(300):  # Collect 300 data points (2 seconds each)
    cpu, memory, disk = psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage('/').percent
    data.append([cpu, memory, disk])
    time.sleep(2)

# Convert data to DataFrame
df = pd.DataFrame(data, columns=['CPU', 'Memory', 'Disk'])

# Train the model to predict CPU usage
X = df[['Memory', 'Disk']]  # Features (Memory and Disk usage)
y = df['CPU']  # Target (CPU usage)

model = LinearRegression()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
