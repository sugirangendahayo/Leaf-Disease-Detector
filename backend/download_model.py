python downloaded_model.py

from ultralytics import YOLO
import os

def verify_model(model_path="weights/leaf_disease.pt"):
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}")
        print("Copy your trained leaf_disease.pt to the weights/ folder")
        return False

    print(f"Loading model from {model_path}...")
    model = YOLO(model_path)

    print("\nModel classes:")
    for i, name in model.names.items():
        print(f"  {i}: {name}")

    print(f"\nModel ready! Detects {len(model.names)} classes.")
    return True

if __name__ == "__main__":
    verify_model()
