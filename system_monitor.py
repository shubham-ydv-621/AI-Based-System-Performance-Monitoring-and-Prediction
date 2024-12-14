import psutil
import time
import json

def get_system_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    disk_info = psutil.disk_usage('/')
    disk_percent = disk_info.percent
    return cpu_percent, memory_percent, disk_percent

def get_data():
    cpu, memory, disk = get_system_stats()
    return json.dumps({
        "cpu": cpu,
        "memory": memory,
        "disk": disk
    })

if __name__ == "__main__":
    try:
        for _ in range(10):  # Limit the loop to 10 iterations
            print(get_data())
            time.sleep(2)  # Wait for 2 seconds before getting stats again
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")
