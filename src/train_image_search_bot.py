import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

def train_image_search_model(train_dir, model_save_path):
    train_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='input'
    )

    base_model = ResNet50(weights='imagenet', include_top=False)
    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        Dense(train_generator.num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(train_generator, epochs=10)
    model.save(model_save_path)

if __name__ == "__main__":
    train_dir = '/workspaces/marketplace_listing/train_data'
    model_save_path = '/workspaces/marketplace_listing/models/image_search_model.h5'
    train_image_search_model(train_dir, model_save_path)
