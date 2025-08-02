import subprocess
import sys
import time
import os

# Helper to launch a process in its own console window (works on Windows)
def run_in_console(cmd, cwd=None):
    if sys.platform.startswith('win'):
        return subprocess.Popen(
            cmd, cwd=cwd, creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    else:
        # Linux/Mac: run in regular process (open terminals separately for full isolation)
        return subprocess.Popen(cmd, cwd=cwd)

processes = []

try:
    # 1. Start MCP server
    processes.append(run_in_console([sys.executable, "mcp_server/server.py"]))

    time.sleep(2)  # Let the server start

    # 2. Start main detection pipeline
    processes.append(run_in_console([sys.executable, "main.py"]))

    time.sleep(2)  # Give detection loop a moment

    # 3. Start Streamlit dashboard
    # Use 'streamlit' executable from your venv's Scripts or bin folder if needed
    if sys.platform.startswith('win'):
        streamlit_cmd = ["streamlit", "run", "dashboard/app.py"]
    else:
        streamlit_cmd = ["streamlit", "run", "dashboard/app.py"]
    processes.append(run_in_console(streamlit_cmd))

    print("All services started. Press Ctrl+C here to stop.")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Shutting down all services...")
    for proc in processes:
        try:
            proc.terminate()
        except Exception:
            pass
    print("Shutdown complete.")
