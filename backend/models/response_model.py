class ResponseModel:
    def format_detections(self, detections):
        """
        Format YOLO detections into the expected API response format
        """
        formatted_detections = []
        
        for detection in detections:
            formatted_detections.append({
                'label': detection['label'],
                'confidence': round(detection['confidence'], 2)
            })
        
        return formatted_detections
