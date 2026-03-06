from flask import Blueprint, request, jsonify
from controllers.detect_controller import DetectController

detect_bp = Blueprint('detect', __name__)

@detect_bp.route('/detect', methods=['POST'])
def detect_disease():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({'error': 'No image file selected'}), 400

        controller = DetectController()
        result     = controller.detect_leaf_disease(image_file)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
