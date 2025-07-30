from django.core.management.base import BaseCommand
from common.utils.trainer import ImageClassifierTrainer
import os

class Command(BaseCommand):
    help = 'Train the animal classifier model'

    def handle(self, *args, **kwargs):
        DATASET_DIR = os.path.join(os.getcwd(), 'datasets', 'animals')
        MODEL_PATH = os.path.join(os.getcwd(), 'models', 'animal_model.h5')
        CLASS_NAMES = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']

        trainer = ImageClassifierTrainer(DATASET_DIR, MODEL_PATH, CLASS_NAMES)
        trainer.train(epochs=10)
        self.stdout.write(self.style.SUCCESS('Animal model trained and saved!'))
