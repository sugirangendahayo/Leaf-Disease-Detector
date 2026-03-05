from services.yolo_service import YOLOService
from utils.image_utils import ImageUtils
from models.response_model import ResponseModel

class DetectController:
    def __init__(self):
        self.yolo_service = YOLOService()
        self.image_utils = ImageUtils()
        self.response_model = ResponseModel()
    
    def detect_leaf_disease(self, image_file):
        try:
            # Convert uploaded file to PIL Image
            pil_image = self.image_utils.file_to_pil_image(image_file)
            
            # Run YOLO detection
            detections = self.yolo_service.detect_diseases(pil_image)
            
            # Format response
            response = self.response_model.format_detections(detections)
            
            return response
            
        except Exception as e:
            raise Exception(f"Detection failed: {str(e)}")
