# Raspberry Pi Camera Setup – Pi Camera Module 2

This guide explains how to configure your Pi Camera Module 2 for use with `libcamera` and this AI detection system.

---

## 📸 Enable the Camera

1. Open Raspberry Pi Configuration:
   ```bash
   sudo raspi-config
   ```

2. Navigate to:
   ```
   Interface Options → Camera → Enable
   ```

3. Reboot your Raspberry Pi:
   ```bash
   sudo reboot
   ```

---

## 🛠️ Test the Camera

Run a quick test with `libcamera-still`:
```bash
libcamera-still -o test.jpg -t 1000
```

- If successful, a photo named `test.jpg` will be saved in your current directory.
- If you get an error, check camera ribbon cable connection.

---

## 📐 Image Size

This project uses:
- Width: 224 px
- Height: 224 px

Make sure any test image matches the model’s input size:
```bash
libcamera-still -o capture.jpg -t 1000 --width 224 --height 224
```

---

## 🔧 Optional: Check Camera Module Connection

Use this to check if the camera is detected:
```bash
libcamera-hello
```

---