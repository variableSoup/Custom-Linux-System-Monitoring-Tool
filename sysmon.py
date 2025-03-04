import psutil
import time
import os

def get_system_metrics():
    """Fetch system resource usage metrics."""
    metrics = {
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Available Memory (MB)": psutil.virtual_memory().available // (1024 * 1024),
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Disk Free Space (GB)": psutil.disk_usage('/').free // (1024 * 1024 * 1024),
        "Network Sent (MB)": psutil.net_io_counters().bytes_sent / (1024 * 1024),
        "Network Received (MB)": psutil.net_io_counters().bytes_recv / (1024 * 1024),
    }
    return metrics

def print_metrics(metrics):
    """Print system metrics in a readable format."""
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen
    print("=" * 40)
    print(" 📊 Real-Time System Monitoring ")
    print("=" * 40)
    for key, value in metrics.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    try:
        while True:
            system_metrics = get_system_metrics()
            print_metrics(system_metrics)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting Monitoring Tool. Goodbye!")