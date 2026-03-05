from ultralytics import YOLO
import os

class YOLOConfig:
    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), '..', 'weights', 'leaf_disease.pt')
        self.model = None
        self.load_model()
    
    def load_model(self):
        try:
            self.model = YOLO(self.model_path)
            print(f"YOLO model loaded successfully from {self.model_path}")
        except Exception as e:
            print(f"Error loading YOLO model: {e}")
            # For demo purposes, create a dummy model if real model doesn't exist
            self.model = None
    
    def get_model(self):
        return self.model

# Global instance
yolo_config = YOLOConfig()
