from config.yolo import yolo_config
import numpy as np
from PIL import Image

DISEASE_DISPLAY_NAMES = {
    "Tomato___Early_blight":                    "Tomato Early Blight",
    "Tomato___Late_blight":                     "Tomato Late Blight",
    "Tomato___healthy":                         "Tomato Healthy",
    "Potato___Early_blight":                    "Potato Early Blight",
    "Potato___Late_blight":                     "Potato Late Blight",
    "Corn_(maize)___Northern_Leaf_Blight":      "Corn Northern Blight",
    "Corn_(maize)___healthy":                   "Corn Healthy",
    "Apple___Apple_scab":                       "Apple Scab",
    "Apple___healthy":                          "Apple Healthy",
}

CONFIDENCE_THRESHOLD = 0.40

class YOLOService:
    def __init__(self):
        self.model = yolo_config.get_model()

    def detect_diseases(self, image: Image.Image):
        if self.model is None:
            raise Exception("Model not loaded. Add weights/leaf_disease.pt")

        image_array = np.array(image)
        results = self.model(image_array, conf=CONFIDENCE_THRESHOLD)

        detections = []
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    confidence = float(box.conf[0])
                    class_id   = int(box.cls[0])
                    raw_label  = self.model.names[class_id]

                    detections.append({
                        'label':      DISEASE_DISPLAY_NAMES.get(raw_label, raw_label),
                        'raw_label':  raw_label,
                        'confidence': round(confidence, 2),
                        'is_healthy': 'healthy' in raw_label.lower()
                    })

        detections.sort(key=lambda x: x['confidence'], reverse=True)
        return detections
