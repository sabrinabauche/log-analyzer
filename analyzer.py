import re
import pandas as pd
from datetime import datetime

def parse_logs(file_path):
    # Expresión regular para extraer la info del log
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (Failed|Successful) login from IP (\d+\.\d+\.\d+\.\d+)'
    data = []

    # Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                timestamp_str, status, ip = match.groups()
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                data.append({'timestamp': timestamp, 'status': status, 'ip': ip})

    # Convertir a DataFrame
    df = pd.DataFrame(data)
    return df
if __name__ == "__main__":
    df_logs = parse_logs("logs/sample_logs.txt")
    print(df_logs.head(10))  # muestra las primeras 10 filas