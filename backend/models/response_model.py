class ResponseModel:
    def format_detections(self, detections):
        formatted = []
        for d in detections:
            formatted.append({
                'label':      d.get('label'),
                'confidence': d.get('confidence'),
                'is_healthy': d.get('is_healthy', False)
            })
        return formatted
