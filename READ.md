# AI Security Camera with Alerts

A real-time Raspberry Pi-based security camera that uses TensorFlow Lite for object detection and triggers alerts via GPIO LED and Discord/Telegram webhooks.

## 🔧 Features
- Local image classification using TFLite and MobileNetV2
- LED turns on for 10 seconds when a target is detected
- Sends alerts to phone/PC via Discord or Telegram webhook
- Runs headless and auto-starts using `systemd`
- Built-in Wi-Fi hotspot mode for field deployment
- Full remote control via SSH (dual-terminal setup)

## 🖥️ Hardware Used
- Raspberry Pi 5
- Pi Camera Module 2
- GPIO LED with 200Ω resistor
- Optional: 7" HDMI touchscreen

## 🧠 Software Stack
- Python 3.11
- TensorFlow Lite Runtime
- ONNX Runtime (optional)
- GPIOZero + libcamera
- `systemd` service for auto-run
- Discord/Telegram webhook API

## 📸 Example Setup
```bash
python3 classify_loop.py
```

## 📂 File Structure
```
ai-camera-alert/
├── classify_loop.py
├── ai-env-requirements.txt
├── camera_config.md
├── systemd-setup.md
├── README.md
└── example_output.jpg
```

## 🛠️ Setup Instructions
1. Clone the repo and activate Python environment:
   ```bash
   git clone https://github.com/quantum-v/ai-camera-alert.git
   cd ai-camera-alert
   source ~/ai-env/bin/activate
   ```

2. Run the inference script:
   ```bash
   python3 classify_loop.py
   ```

3. For auto-run on boot, see `systemd-setup.md`

## 📲 Demo
![Example Output](example_output.jpg)

## 🧠 Author
Quantum Richardson  
[GitHub Profile](https://github.com/quantum-v)
