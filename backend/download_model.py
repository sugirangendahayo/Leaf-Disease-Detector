from ultralytics import YOLO
import os
import shutil

os.makedirs("weights", exist_ok=True)

print("Downloading YOLOv8 model...")

# Downloads automatically, no account needed
model = YOLO("yolov8n.pt")

shutil.copy("yolov8n.pt", "weights/leaf_disease.pt")

print("Model saved to weights/leaf_disease.pt")
print("Your app is ready to run!")