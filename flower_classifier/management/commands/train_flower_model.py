from django.core.management.base import BaseCommand
from common.utils.trainer import ImageClassifierTrainer
import os

class Command(BaseCommand):
    help = 'Train the flower classifier model'

    def handle(self, *args, **kwargs):
        DATASET_DIR = os.path.join(os.getcwd(), 'datasets', 'flowers')
        MODEL_PATH = os.path.join(os.getcwd(), 'models', 'flower_model.h5')
        CLASS_NAMES = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

        trainer = ImageClassifierTrainer(DATASET_DIR, MODEL_PATH, CLASS_NAMES)
        trainer.train(epochs=10)
        self.stdout.write(self.style.SUCCESS('Flower model trained and saved!'))
