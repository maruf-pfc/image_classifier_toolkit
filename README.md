# Image Classifier Toolkit

A Django-based web application with multiple image classification projects including flower, animal, fruit, emotion, vehicle, and digit classifiers. Each classifier has its own model and training pipeline using TensorFlow/Keras.

## Project Structure

```txt
image_classifier_toolkit/
├── common/                    # Common utilities, e.g., training helper classes
├── config/                    # Project configuration files (settings, urls, etc.)
├── datasets/                  # Dataset folders for different classifiers
│ ├── flowers/
│ │ ├── daisy/
│ │ ├── dandelion/
│ │ ├── rose/
│ │ ├── sunflower/
│ │ └── tulip/
│ ├── animals/
│ ├── fruits/
│ ├── emotions/
│ ├── vehicles/
│ └── digits/
├── models/                    # Saved trained model files (.h5)
│ ├── flower_model.h5
│ ├── animal_model.h5
│ ├── fruit_model.h5
│ ├── emotion_model.h5
│ ├── vehicle_model.h5
│ └── digit_model.h5
├── media/                     # Uploaded media files (images for prediction)
├── flower_classifier/         # Django app for flower classification
├── animal_classifier/         # Django app for animal classification
├── fruit_classifier/          # Django app for fruit classification
├── emotion_classifier/        # Django app for emotion classification
├── vehicle_classifier/        # Django app for vehicle classification
├── digit_classifier/          # Django app for digit classification
├── manage.py                  # Django management script
└── README.md
```

## Dataset Downloads

You need to [download](https://drive.google.com/drive/folders/157V2o8Y8Mb4h74YgcWNvLV490ZZpxmJ1?usp=drive_link) datasets for each classifier and place them inside the `datasets` folder as shown above.

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/maruf-pfc/image_classifier_toolkit.git
   cd image_classifier_toolkit
   ```

2. **Create and activate a Python virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate   # Linux/macOS
   # .\env\Scripts\activate  # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Make sure you have TensorFlow installed and compatible with your environment.**

## Training Models

Each classifier has a custom management command to train its model.

Example for **Flower Classifier**:

```bash
python3 manage.py train_flower_model
```

Similarly, run commands for other classifiers, e.g.:

```bash
python3 manage.py train_animal_model
python3 manage.py train_fruit_model
python3 manage.py train_emotion_model
python3 manage.py train_vehicle_model
python3 manage.py train_digit_model
```

**Note:**

- Ensure the corresponding dataset is available inside `datasets/<classifier_name>/` folder before training.
- Models will be saved in the `models/` directory.

## Running the Project

Start the Django development server:

```bash
python3 manage.py runserver
```

Open your browser and visit: `http://127.0.0.1:8000/`

The home page lists all available classifiers with links to their prediction pages.

## Using the Web App

- On the classifier page (e.g., Flower Classifier), upload an image.
- The app will show the uploaded image, run prediction using the trained model, and display the predicted class with confidence.
- You can navigate back to home anytime.

## Flower Prediction Demo

![Predict Flower](./images/Predict%20Flower.png)

## Notes

- Uploaded images are stored in the `media/` folder.
- Static files should be collected or served correctly in production.
- For large datasets or training on GPU, consider using Google Colab or a powerful machine.
- Keep your dataset folders organized to avoid `flow_from_directory` errors during training.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

MIT License © [Md. Maruf Sarker](https://github.com/maruf-pfc)

## Contact

If you have questions or want to collaborate, reach out:

- Email: [mdmarufsarker.mms@gmail.com](mailto:mdmarufsarker.mms@gmail.com)
- GitHub: [https://github.com/maruf-pfc](https://github.com/maruf-pfc)
- Twitter: [@md_marufsarker](https://twitter.com/md_marufsarker)
