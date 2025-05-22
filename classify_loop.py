import time
import numpy as np
from PIL import Image
from gpiozero import LED
from tflite_runtime.interpreter import Interpreter
import subprocess

# GPIO Setup
led = LED(17)  # Use GPIO17 (physical pin 11)

# Load labels
with open("labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Load TFLite model
interpreter = Interpreter(model_path="mobilenet_v2.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

def capture_image():
    img_path = "/tmp/capture.jpg"
    subprocess.run(["libcamera-still", "-o", img_path, "-t", "1000", "--width", str(width), "--height", str(height)], check=True)
    return img_path

def preprocess_image(image_path):
    img = Image.open(image_path).resize((width, height))
    input_data = np.expand_dims(np.array(img, dtype=np.uint8), axis=0)
    return input_data

def predict(input_data):
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    top_result = np.argmax(output_data)
    confidence = output_data[top_result]
    return labels[top_result], confidence

def main():
    print("📷 AI Detection Started. Press Ctrl+C to stop.")
    try:
        while True:
            image_path = capture_image()
            input_data = preprocess_image(image_path)
            label, confidence = predict(input_data)

            print(f"🧠 Detected: {label} ({confidence:.2f})")

            if label.lower() == "person" and confidence > 0.6:
                print("💡 Target detected! Activating LED.")
                led.on()
                time.sleep(10)
                led.off()
            else:
                time.sleep(2)
    except KeyboardInterrupt:
        print("🛑 Stopped.")

if __name__ == "__main__":
    main()