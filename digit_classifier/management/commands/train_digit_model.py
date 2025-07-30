from django.core.management.base import BaseCommand
from common.utils.trainer import ImageClassifierTrainer
import os

class Command(BaseCommand):
    help = 'Train the digit classifier model'

    def handle(self, *args, **kwargs):
        DATASET_DIR = os.path.join(os.getcwd(), 'datasets', 'digits')
        MODEL_PATH = os.path.join(os.getcwd(), 'models', 'digit_model.h5')
        CLASS_NAMES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        trainer = ImageClassifierTrainer(DATASET_DIR, MODEL_PATH, CLASS_NAMES)
        trainer.train(epochs=10)
        self.stdout.write(self.style.SUCCESS('digit model trained and saved!'))
