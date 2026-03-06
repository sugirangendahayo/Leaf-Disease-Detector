from services.yolo_service import YOLOService
from models.response_model import ResponseModel
from utils.image_utils import ImageUtils

class DetectController:
    def __init__(self):
        self.yolo_service   = YOLOService()
        self.response_model = ResponseModel()
        self.image_utils    = ImageUtils()

    def detect_leaf_disease(self, image_file):
        image      = self.image_utils.file_to_pil_image(image_file)
        detections = self.yolo_service.detect_diseases(image)
        formatted  = self.response_model.format_detections(detections)

        return {
            'success':    True,
            'detections': formatted,
            'count':      len(formatted),
            'message':    self._get_message(formatted)
        }

    def _get_message(self, detections):
        if not detections:
            return "No diseases detected. Leaf appears healthy or image unclear."
        diseases = [d for d in detections if not d.get('is_healthy')]
        healthy  = [d for d in detections if d.get('is_healthy')]
        if diseases:
            top = diseases[0]
            return f"Detected: {top['label']} ({int(top['confidence']*100)}% confidence)"
        elif healthy:
            return "Leaf appears healthy!"
        return "Detection complete."
