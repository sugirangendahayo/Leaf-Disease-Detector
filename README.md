# Leaf Disease Detection Mobile App

A complete mobile application for detecting plant leaf diseases using YOLO computer vision and React Native.

## Architecture

The app follows a client-server architecture:

- **Frontend**: React Native + Expo mobile app for image capture and result display
- **Backend**: Python Flask API with YOLO for disease detection
- **Communication**: HTTP REST API with multipart image uploads

## Project Structure

```
leaf-disease-detector/
├── backend/                 # Python Flask + YOLO backend
│   ├── app.py              # Flask app entry point
│   ├── config/
│   │   └── yolo.py         # YOLO model configuration
│   ├── routes/
│   │   └── detect.py       # API routes
│   ├── controllers/
│   │   └── detect_controller.py  # Request handling
│   ├── services/
│   │   └── yolo_service.py # YOLO inference logic
│   ├── models/
│   │   └── response_model.py     # Response formatting
│   ├── utils/
│   │   └── image_utils.py  # Image processing helpers
│   ├── weights/
│   │   └── leaf_disease.pt # YOLO model weights
│   └── requirements.txt
└── frontend/               # React Native + Expo frontend
    ├── App.js
    ├── app.json
    ├── package.json
    └── src/
        ├── screens/
        │   └── ScanScreen.js     # Main scanning screen
        ├── services/
        │   └── api.js           # API communication
        ├── components/
        │   └── ResultCard.js    # Result display component
        ├── utils/
        │   └── permissions.js   # Camera permissions
        └── constants/
            └── config.js        # App configuration
```

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add YOLO model (optional):**
   - Place your trained `leaf_disease.pt` file in `backend/weights/`
   - If no model is provided, the app will use dummy data for demonstration

5. **Start the backend server:**
   ```bash
   python app.py
   ```
   
   The server will run on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the Expo development server:**
   ```bash
   npm start
   ```

4. **Run the app:**
   - **iOS**: Press `i` in the terminal or use Expo Go app
   - **Android**: Press `a` in the terminal or use Expo Go app
   - **Web**: Press `w` to run in browser

## Important Configuration

### For Physical Device Testing

When running on a physical device (not emulator), update the API URL in `frontend/src/constants/config.js`:

```javascript
// Replace with your computer's IP address
export const API_BASE_URL = 'http://YOUR_COMPUTER_IP:5000/api';
```

To find your IP address:
- **Windows**: Run `ipconfig` in command prompt
- **Mac/Linux**: Run `ifconfig` or `ip addr` in terminal

## Request → Response Flow

1. **User Action**: User captures/selects leaf image in the mobile app
2. **Frontend Request**: App sends POST request to `/api/detect` with image data
3. **Backend Processing**: 
   - Flask receives multipart image upload
   - Image is converted to PIL format
   - YOLO model runs inference
   - Results are formatted as JSON
4. **Response**: Backend returns JSON array with detected diseases:
   ```json
   [
     {
       "label": "leaf_rust",
       "confidence": 0.92
     }
   ]
   ```
5. **Frontend Display**: App shows disease name and confidence with visual indicators

## Features

- **Camera Integration**: Take photos directly from the app
- **Gallery Upload**: Select existing images from device gallery
- **Real-time Detection**: YOLO-based disease identification
- **Confidence Scoring**: Visual confidence indicators with color coding
- **Error Handling**: Comprehensive error messages and network handling
- **Responsive Design**: Clean, modern UI optimized for mobile devices

## Dependencies

### Backend
- Flask: Web framework
- Ultralytics: YOLO model implementation
- OpenCV/PIL: Image processing
- Flask-CORS: Cross-origin requests

### Frontend
- React Native: Mobile framework
- Expo: Development platform
- React Navigation: Navigation handling
- Axios: HTTP client
- React Native Image Picker: Camera/gallery access

## Troubleshooting

### Common Issues

1. **Backend connection refused**: Ensure Flask server is running on port 5000
2. **Network timeout**: Check firewall settings and network connectivity
3. **Camera permission denied**: Grant camera permissions in device settings
4. **Model loading error**: Verify YOLO model file path and format

### Development Tips

- Use Expo Go app for quick testing on physical devices
- Test with various leaf images for better model validation
- Monitor backend logs for debugging detection issues
- Use React DevTools for frontend debugging

## Production Deployment

For production deployment:

1. **Backend**: Deploy Flask app to cloud service (AWS, Google Cloud, Heroku)
2. **Frontend**: Build standalone app using Expo EAS Build
3. **Model Optimization**: Compress YOLO model for mobile performance
4. **Security**: Add authentication and rate limiting to API endpoints
