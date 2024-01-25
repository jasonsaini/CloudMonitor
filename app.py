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
        Message = "High Memory AND High CPU Utilization"
    
    return render_template("index.html", cpu_percent=cpu_percentage, mem_percent=mem_percentage, message=Message)
        
if __name__ == '__main__':
    app.run(debug = True, host= '0.0.0.0')