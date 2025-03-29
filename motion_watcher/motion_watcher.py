import requests
import time
import subprocess
import os
from dotenv import load_dotenv
from datetime import datetime

# Load .env variables
load_dotenv()

HA_URL = os.getenv("HA_URL")
HA_TOKEN = os.getenv("HA_TOKEN")
CANISTER_NAME = os.getenv("CANISTER_NAME")
NETWORK = os.getenv("NETWORK")

last_changed_saved = None
LOG_FILE = "motion_watcher/logs/motion_watcher.log"

headers_ha = {
    "Authorization": HA_TOKEN,
    "Content-Type": "application/json"
}

def write_log(message):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def get_motion_state():
    try:
        response = requests.get(HA_URL, headers=headers_ha)
        data = response.json()
        return data["state"], data["last_changed"]
    except Exception as e:
        write_log(f"❗️ API error: {e}")
        return None, None

def log_to_canister(state, time_value):
    try:
        command = [
            "dfx", "canister", "call", "--network", NETWORK, CANISTER_NAME, "log_event",
            f'("{state}", "{time_value}")'
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            write_log(f"✅ Event logged: {state} at {time_value}")
        else:
            write_log(f"❗️ Canister call error: {result.stderr.strip()}")
    except Exception as e:
        write_log(f"❗️ Error: {e}")

if __name__ == "__main__":
    write_log("🚀 Motion Watcher started")
    while True:
        state, last_changed = get_motion_state()
        if state and last_changed and last_changed != last_changed_saved:
            log_to_canister(state, last_changed)
            last_changed_saved = last_changed
        time.sleep(10)
