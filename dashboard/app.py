# dashboard/app.py

import streamlit as st
import requests
import time

st.set_page_config(
    page_title="SmartWatchdog AI Dashboard",
    layout="wide",
)

st.title("🐾 SmartWatchdog AI – Live Surveillance Alerts")
st.caption("Real-time security events and suspicious activity alerts")

# URL of your MCP server
MCP_SERVER_URL = "http://localhost:8000/report/latest"

alert_placeholder = st.empty()
json_placeholder = st.empty()

def get_latest_alert():
    try:
        resp = requests.get(MCP_SERVER_URL, timeout=2)
        if resp.status_code == 200 and resp.content:
            return resp.json()
    except Exception as e:
        st.error(f"Could not connect to MCP server: {e}")
    return None

st.sidebar.header("Settings")
refresh_interval = st.sidebar.slider("Refresh interval (seconds)", 1, 10, 2)

while True:
    alert = get_latest_alert()
    alert_placeholder.empty()
    json_placeholder.empty()
    if alert:
        if alert.get("suspicious"):
            alert_placeholder.error(f"⚠️ ALERT ({alert.get('reason', 'Suspicious activity')}): {alert.get('objects_detected')}")
        else:
            alert_placeholder.success("✅ No suspicious activity detected.")
        # Show raw JSON report as well
        json_placeholder.json(alert)
    else:
        alert_placeholder.info("Waiting for new reports from MCP server...")
    time.sleep(refresh_interval)
