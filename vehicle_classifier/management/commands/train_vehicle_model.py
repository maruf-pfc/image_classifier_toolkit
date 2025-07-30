from django.core.management.base import BaseCommand
from common.utils.trainer import ImageClassifierTrainer
import os

class Command(BaseCommand):
    help = 'Train the vehicle classifier model'

    def handle(self, *args, **kwargs):
        DATASET_DIR = os.path.join(os.getcwd(), 'datasets', 'vehicles')
        MODEL_PATH = os.path.join(os.getcwd(), 'models', 'vehicle_model.h5')
        CLASS_NAMES = ['bus', 'family_sedan', 'fire_engine', 'heavy_truck', 'jeep', 'minibus', 'racing_car', 'SUV', 'taxi', 'truck']

        trainer = ImageClassifierTrainer(DATASET_DIR, MODEL_PATH, CLASS_NAMES)
        trainer.train(epochs=10)
        self.stdout.write(self.style.SUCCESS('vehicle model trained and saved!'))
