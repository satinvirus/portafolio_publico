import psutil
import time
import os
import subprocess
from datetime import datetime

def actualizar_dashboard(cpu, ram):
    ahora = datetime.now().strftime("%H:%M:%S")
    
    # Leemos la plantilla (asegúrate de que el nombre coincida con tu archivo html)
    with open("index.html", "r") as f:
        html_content = f.read()
    
    # Reemplazamos los valores
    html_content = html_content.replace("{{CPU_USO}}", str(cpu))
    html_content = html_content.replace("{{RAM_USO}}", str(ram))
    html_content = html_content.replace("{{HORA}}", ahora)
    
    # Guardamos el archivo final actualizado
    with open("dashboard_vivo.html", "w") as f:
        f.write(html_content)

def monitorear():
    print("--- MONITOR INICIADO (Generando dashboard_vivo.html) ---")
    try:
        while True:
            cpu_uso = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            
            # 1. Alerta en Bash (Si pasa de 80)
            if cpu_uso > 80:
                subprocess.run(["./alerta.sh"])
            
            # 2. Actualizar Dashboard Web
            actualizar_dashboard(cpu_uso, ram)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Datos actualizados en el Dashboard.")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitor detenido.")

if __name__ == "__main__":
    monitorear()