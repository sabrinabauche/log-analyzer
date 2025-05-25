# 🛡️ Log Analyzer – Cybersecurity Project with Streamlit

This is a simple log analysis project built with Python and Streamlit. It simulates login attempts and visualizes potentially suspicious behavior, such as multiple failed logins from the same IP address.

## 🔍 What it does

- Simulates login data with random timestamps, IP addresses, and login results (success/failure).
- Extracts and structures that data using Python (regex + pandas).
- Displays an interactive dashboard to:
  - Show all logs in a table.
  - Visualize failed login attempts per IP.
  - Highlight suspicious IPs with more than 5 failed attempts.
 
✨ Features demonstrated
- Python scripting and data simulation
- Log parsing with regular expressions
- Data analysis with pandas
- Interactive dashboards with Streamlit
- Basic anomaly detection logic (suspicious IP detection)

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/8c098971-93c9-4e58-b609-83dc75200453)

## 🧱 Project Structure
log-analyzer/
├── analyzer.py # Parses and structures log data
├── app.py # Streamlit dashboard interface
├── generate_logs.py # Simulates and generates 100 login events
├── logs/
│ └── sample_logs.txt # Generated log file
├── requirements.txt # List of Python dependencies
└── .gitignore # Files excluded from version control


## 🚀 How to run it locally

### 1. Clone the repository
git clone https://github.com/sabrinabauche/log-analyzer.git
cd log-analyzer

2. Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate    # On Windows

3. Install the required libraries
pip install -r requirements.txt

4. Run the app
streamlit run app.py
