# Auto-Start AI Detection Script with systemd

This guide explains how to run `classify_loop.py` automatically at boot using `systemd`.

---

## 🗂️ Step 1: Create a systemd Service File

Open a terminal on your Raspberry Pi and run:

```bash
sudo nano /etc/systemd/system/ai-camera.service
```

Paste in the following:
```ini
[Unit]
Description=AI Camera Detection Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/raspberrypi/ai-camera-alert/classify_loop.py
WorkingDirectory=/home/raspberrypi/ai-camera-alert
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

> ⚠️ Make sure the paths match where your files are stored.

---

## 💾 Step 2: Enable and Start the Service

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable ai-camera.service
sudo systemctl start ai-camera.service
```

---

## ✅ Step 3: Check Status

To see if it’s running:
```bash
sudo systemctl status ai-camera.service
```

To stop or restart:
```bash
sudo systemctl stop ai-camera.service
sudo systemctl restart ai-camera.service
```

---

## 🧹 Optional: Disable Auto-Start

```bash
sudo systemctl disable ai-camera.service
```

This will prevent it from launching automatically on boot.