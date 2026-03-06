"""
Download a proper plant disease detection model from Roboflow
"""
import os
import requests
from roboflow import Roboflow

# Create weights directory
os.makedirs("weights", exist_ok=True)

print("🌱 Setting up plant disease detection model...")

try:
    # Initialize Roboflow with your API key
    rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")  # Replace with your key
    
    # Access a public plant disease dataset
    project = rf.workspace("plant-diseases").project("plant-disease-detection")
    version = project.version(1)
    
    # Download the YOLOv8 model
    version.download("yolov8")
    
    # Find and copy the model
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".pt") and "weights" not in root:
                src = os.path.join(root, file)
                dst = os.path.join("weights", "leaf_disease.pt")
                os.rename(src, dst)
                print(f"✅ Plant disease model saved to: {dst}")
                print("🎯 This model is trained specifically for plant diseases!")
                return True
    
    print("❌ No model file found")
    return False

except Exception as e:
    print(f"❌ Error downloading plant disease model: {e}")
    print("\n📋 Solutions:")
    print("1. Get a Roboflow API key from https://roboflow.com/")
    print("2. Find a public plant disease dataset")
    print("3. Train your own model on plant disease images")
    print("4. Use the dummy data for now (app will work but not accurate)")
    
    # Create placeholder for development
    placeholder_path = "weights/leaf_disease.pt"
    with open(placeholder_path, 'wb') as f:
        f.write(b'placeholder')
    print(f"📄 Created placeholder: {placeholder_path}")
    return False
