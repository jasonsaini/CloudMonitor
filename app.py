import psutil
from flask import Flask, render_template

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percentage = psutil.cpu_percent(interval=1)
    mem_percentage = psutil.virtual_memory().percent
    Message = None
    if cpu_percentage > CPU_THRESHOLD:
        Message = "High CPU Utilization"
    if mem_percentage > MEM_THRESHOLD:
        Message = "High Memory Utilization"
    if mem_percentage > MEM_THRESHOLD and cpu_percentage > CPU_THRESHOLD:
        message = "Hight Memory AND High CPU Utilization"
    return f"CPU Utilization: {cpu_percentage}, Memory Utilization: {mem_percentage}"
        
if __name__ == '__main__':
    app.run(debug = True, host= '0.0.0.0')