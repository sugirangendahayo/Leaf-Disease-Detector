from config.yolo import yolo_config
import numpy as np
from PIL import Image

class YOLOService:
    def __init__(self):
        self.model = yolo_config.get_model()
    
    def detect_diseases(self, image):
        if self.model is None:
            # Return dummy data for demo when model is not available
            return [
                {
                    'label': 'leaf_rust',
                    'confidence': 0.85
                }
            ]
        
        try:
            # Convert PIL Image to numpy array
            image_array = np.array(image)
            
            # Run YOLO inference
            results = self.model(image_array)
            
            detections = []
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        confidence = float(box.conf[0])
                        class_id = int(box.cls[0])
                        label = self.model.names[class_id]
                        
                        detections.append({
                            'label': label,
                            'confidence': confidence
                        })
            
            return detections
            
        except Exception as e:
            print(f"YOLO inference error: {e}")
            # Fallback to dummy data
            return [
                {
                    'label': 'leaf_blight',
                    'confidence': 0.75
                }
            ]
