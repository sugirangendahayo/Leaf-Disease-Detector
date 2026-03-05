from PIL import Image
import io

class ImageUtils:
    def file_to_pil_image(self, file_storage):
        """
        Convert Flask FileStorage to PIL Image
        """
        try:
            # Read file content
            file_bytes = file_storage.read()
            
            # Create PIL Image from bytes
            image = Image.open(io.BytesIO(file_bytes))
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            return image
            
        except Exception as e:
            raise Exception(f"Failed to process image: {str(e)}")
    
    def validate_image(self, image):
        """
        Validate image format and size
        """
        try:
            # Check if image is valid
            image.verify()
            
            # Reset file pointer after verify
            image.seek(0)
            
            return True
            
        except Exception:
            return False
