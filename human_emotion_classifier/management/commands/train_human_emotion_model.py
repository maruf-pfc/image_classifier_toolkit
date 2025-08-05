from django.core.management.base import BaseCommand
from common.utils.trainer import ImageClassifierTrainer
import os

class Command(BaseCommand):
    help = 'Train the human emotion classifier model'

    def handle(self, *args, **kwargs):
        DATASET_DIR = os.path.join(os.getcwd(), 'datasets', 'emotions')
        MODEL_PATH = os.path.join(os.getcwd(), 'models', 'human_emotion_model.h5')
        CLASS_NAMES = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

        trainer = ImageClassifierTrainer(DATASET_DIR, MODEL_PATH, CLASS_NAMES)
        trainer.train(epochs=10)
        self.stdout.write(self.style.SUCCESS('Human emotion model trained and saved!'))
