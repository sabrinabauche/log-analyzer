import random
from datetime import datetime, timedelta

# Configuración
statuses = ["Failed", "Successful"]
ips = [f"192.168.1.{i}" for i in range(1, 21)]  # 20 IPs del 192.168.1.1 al 192.168.1.20
num_logs = 100  # Cantidad de líneas a generar
start_time = datetime.now()

log_lines = []

# Generar los logs
for i in range(num_logs):
    time = start_time + timedelta(seconds=i * 30)  # cada 30 segundos
    status = random.choices(statuses, weights=[0.7, 0.3])[0]  # 70% failed, 30% success
    ip = random.choice(ips)
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {status} login from IP {ip}"
    log_lines.append(line)

# Guardar en el archivo
with open("logs/sample_logs.txt", "w") as f:
    f.write("\n".join(log_lines))

print("✅ Archivo 'sample_logs.txt' generado con 100 líneas.")