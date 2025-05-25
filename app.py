import streamlit as st
import pandas as pd
from analyzer import parse_logs

st.set_page_config(page_title="Log Analyzer", page_icon="🛡️", layout="wide")

# Título principal
st.title("🛡️ Analizador de Logs de Seguridad")
st.write("Este dashboard analiza intentos de inicio de sesión fallidos y exitosos por dirección IP.")

# Leer los logs
log_file = "logs/sample_logs.txt"
df_logs = parse_logs(log_file)

# Mostrar los logs
st.subheader("📋 Tabla de Logs")
st.dataframe(df_logs)

# Intentos fallidos por IP
st.subheader("📊 Intentos Fallidos por IP")
failed = df_logs[df_logs['status'] == 'Failed']
failed_counts = failed['ip'].value_counts().reset_index()
failed_counts.columns = ['IP', 'Intentos Fallidos']
st.bar_chart(failed_counts.set_index('IP'))

# IPs sospechosas (más de 5 intentos fallidos)
st.subheader("🚨 IPs Sospechosas")
umbral = 5
suspicious = failed_counts[failed_counts['Intentos Fallidos'] > umbral]

if not suspicious.empty:
    st.warning("Se detectaron IPs con más de 5 intentos fallidos:")
    st.table(suspicious)
else:
    st.success("No hay IPs sospechosas registradas 🎉")