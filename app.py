from flask import Flask, jsonify, render_template
import psutil
import pickle

# Load the trained AI model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

def get_system_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    disk_info = psutil.disk_usage('/')
    disk_percent = disk_info.percent
    return cpu_percent, memory_percent, disk_percent

def get_prediction(memory, disk):
    prediction = model.predict([[memory, disk]])
    return prediction[0]

@app.route('/')
def index():
    cpu, memory, disk = get_system_stats()
    prediction = get_prediction(memory, disk)
    return render_template('index.html', cpu=cpu, memory=memory, disk=disk, prediction=prediction)

@app.route('/stats')
def stats():
    cpu, memory, disk = get_system_stats()
    prediction = get_prediction(memory, disk)
    # Return stats as JSON
    return jsonify({
        'cpu': cpu,
        'memory': memory,
        'disk': disk,
        'prediction': prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
