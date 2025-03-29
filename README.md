
# 🚀 Motion Logger

## 🎯 Description

**Motion Logger** is a decentralized motion event logging system built on the **Internet Computer** blockchain.  
The system records every state change detected by a motion sensor into a public and transparent on-chain journal.

This project was developed as part of the [Kyiv-Mohyla Academy ICP Hackathon](https://github.com/KyivMohylaAcademy/ICPMasters/blob/main/HACKATHON.md).

---

## 🟢 How It Works

1. A motion sensor is connected to **Home Assistant**
2. A Python script periodically (every 10 seconds) polls the Home Assistant API
3. When the sensor state changes, or the timestamp of the last change is updated, the event is logged into a canister on the Internet Computer
4. The event journal is publicly accessible via **Candid UI**

---

## 🌐 Live Demo

**Candid UI:**  
[https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.icp0.io/?id=wreye-4qaaa-aaaap-qpywa-cai](https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.icp0.io/?id=wreye-4qaaa-aaaap-qpywa-cai)

---

## 📂 Project Structure

```
motion-logger/
├── src/
│   └── motion-logger-backend/
│       └── main.mo              # Canister code (Motoko)
├── motion_watcher/
│   ├── motion_watcher.py        # Python watcher script
│   ├── run.sh                   # Background launcher script
│   ├── .env                     # API and canister configuration
│   └── logs/
│       └── motion_watcher.log   # Event logs
├── dfx.json
├── canister_ids.json
├── .gitignore
├── README.md
```

---

## ⚙️ How To Use

### 1️⃣ Deploy Canister

```bash
dfx canister create --network ic motion-logger-backend
dfx build
dfx deploy --network ic
```

---

### 2️⃣ Configure Python Watcher

1. Create a `.env` file in `motion_watcher/`:

```
HA_URL="https://ha-home-server.troshab.com/api/states/binary_sensor.entrance_near_kitchen_ceiling_presence_sensor_occupancy"
HA_TOKEN="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." # Your Home Assistant token
CANISTER_NAME=motion-logger-backend
NETWORK=ic
```

2. Make `run.sh` executable:

```bash
chmod +x motion_watcher/run.sh
```

3. Start the watcher script:

```bash
./motion_watcher/run.sh
```

4. Check logs:

```bash
cat motion_watcher/logs/motion_watcher.log
```

---

### 3️⃣ View Event Journal

You can check logged events:

**Candid UI:**  
[https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.icp0.io/?id=wreye-4qaaa-aaaap-qpywa-cai](https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.icp0.io/?id=wreye-4qaaa-aaaap-qpywa-cai)

**CLI:**

```bash
dfx canister call --network ic motion-logger-backend get_events
```

---

## 💡 Tech Stack

- 🟢 Internet Computer
- 📄 Motoko
- 🐍 Python 3
- 🏠 Home Assistant API
- 🔐 Canister Smart Contract

---

## 🧩 Purpose

This project demonstrates how blockchain technology can be used to log real-world sensor events (motion detection) in a decentralized, transparent, and immutable journal.

---
