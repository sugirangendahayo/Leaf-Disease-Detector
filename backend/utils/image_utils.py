from PIL import Image
import io

class ImageUtils:
    def file_to_pil_image(self, file_storage):
        try:
            file_bytes = file_storage.read()
            image = Image.open(io.BytesIO(file_bytes))
            if image.mode != 'RGB':
                image = image.convert('RGB')
            return image
        except Exception as e:
            raise Exception(f"Failed to process image: {str(e)}")

    def validate_image(self, image):
        try:
            image.verify()
            image.seek(0)
            return True
        except Exception:
            return False
