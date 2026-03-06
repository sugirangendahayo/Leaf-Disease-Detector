from ultralytics import YOLO
import os

class YOLOConfig:
    def __init__(self):
        self.model_path = "weights/leaf_disease.pt"
        self._model = None

    def get_model(self):
        if self._model is None:
            if os.path.exists(self.model_path):
                print(f"Loading leaf disease model from {self.model_path}")
                self._model = YOLO(self.model_path)
            else:
                print(f"Model not found at {self.model_path}")
                print("Run downloaded_model.py or copy trained model there.")
        return self._model

yolo_config = YOLOConfig()
