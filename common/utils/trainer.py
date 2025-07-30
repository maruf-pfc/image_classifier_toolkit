from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.applications import MobileNetV2 # type: ignore
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D # type: ignore
from tensorflow.keras.models import Model # type: ignore

class ImageClassifierTrainer:
    def __init__(self, dataset_dir, output_model_path, class_names, img_size=(224,224), batch_size=32):
        self.dataset_dir = dataset_dir
        self.output_model_path = output_model_path
        self.class_names = class_names
        self.img_size = img_size
        self.batch_size = batch_size

    def prepare_data(self):
        datagen = ImageDataGenerator(validation_split=0.2,
                                     rescale=1./255,
                                     horizontal_flip=True,
                                     rotation_range=20)
        
        self.train_generator = datagen.flow_from_directory(
            self.dataset_dir,
            target_size=self.img_size,
            batch_size=self.batch_size,
            classes=self.class_names,
            subset='training'
        )
        self.val_generator = datagen.flow_from_directory(
            self.dataset_dir,
            target_size=self.img_size,
            batch_size=self.batch_size,
            classes=self.class_names,
            subset='validation'
        )

    def build_model(self):
        base_model = MobileNetV2(input_shape=(*self.img_size, 3), include_top=False, weights='imagenet')
        base_model.trainable = False

        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(128, activation='relu')(x)
        predictions = Dense(len(self.class_names), activation='softmax')(x)

        self.model = Model(inputs=base_model.input, outputs=predictions)
        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def train(self, epochs=10):
        self.prepare_data()
        self.build_model()

        self.model.fit(
            self.train_generator,
            validation_data=self.val_generator,
            epochs=epochs
        )
        self.model.save(self.output_model_path)
        print(f"Model saved to {self.output_model_path}")
