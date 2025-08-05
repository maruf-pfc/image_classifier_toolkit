from django.shortcuts import render
from django.conf import settings
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
from django.core.files.storage import FileSystemStorage

MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'human_emotion_model.h5')
model = None

def get_model():
    global model
    if model is None:
        if os.path.exists(MODEL_PATH):
            model = load_model(MODEL_PATH)
        else:
            raise Exception(f"Model not found. Please train the model first: {MODEL_PATH}")
    return model

def predict_human_emotion(request):
    result = None
    uploaded_image_url = None

    supported_classes = [
        'Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 
        'Sad', 'Surprise'
    ]

    if request.method == 'POST':
        img_file = request.FILES.get('image')
        if img_file:
            # Save image temporarily
            fs = FileSystemStorage()
            filename = fs.save(img_file.name, img_file)
            uploaded_image_url = fs.url(filename)

            # Preprocess
            img_path = os.path.join(settings.MEDIA_ROOT, filename)
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Predict
            model = get_model()
            preds = model.predict(img_array)
            pred_index = np.argmax(preds[0])
            confidence = preds[0][pred_index]
            class_names = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
            predicted_class = class_names[pred_index]
            result = f"Prediction: {predicted_class} ({confidence*100:.2f}%)"

    return render(request, 'human_emotion_classifier/predict.html', {
        'result': result,
        'uploaded_image_url': uploaded_image_url,
        'supported_classes': supported_classes
    })
