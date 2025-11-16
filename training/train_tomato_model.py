from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from collections import Counter


# ---- SETTINGS ----
DATA_DIR = "../data/tomato"
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 10            # head training epochs
FINE_TUNE = True       # whether to run fine-tuning stage
FINE_TUNE_EPOCHS = 10  # additional epochs for fine-tuning
FINE_TUNE_AT = 100     # layer index in base_model from which to unfreeze
MODEL_DIR = "../saved_models"

os.makedirs(MODEL_DIR, exist_ok=True)


# ---- DATASET ----
datagen = ImageDataGenerator(
    rescale=1/255.0,
    validation_split=0.2,
    horizontal_flip=True,
    rotation_range=20,
    zoom_range=0.2
)

train_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    subset='training'
)

val_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    subset='validation'
)

num_classes = train_gen.num_classes

# Save class indices mapping for reproducible inference
class_indices_path = os.path.join(MODEL_DIR, "class_indices.json")
with open(class_indices_path, "w", encoding="utf-8") as f:
    json.dump(train_gen.class_indices, f, indent=2)
print(f"Saved class_indices to {class_indices_path}")


# Compute class weights to help with imbalanced datasets
try:
    labels_array = train_gen.classes  # numpy array of labels per sample
    counts = np.bincount(labels_array)
    total = labels_array.shape[0]
    class_weight = {i: total / (len(counts) * counts[i]) for i in range(len(counts))}
    print("Computed class_weight:", class_weight)
except Exception:
    class_weight = None
    print("Could not compute class_weight, proceeding without it")


# ---- MODEL (base) ----
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)
output = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

# Compile for head training (higher lr)
model.compile(
    optimizer=Adam(learning_rate=1e-3),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


# ---- CALLBACKS ----
best_path = os.path.join(MODEL_DIR, "tomato_disease_model_best.h5")
checkpoint_cb = ModelCheckpoint(best_path, monitor='val_accuracy', save_best_only=True, verbose=1)
earlystop_cb = EarlyStopping(monitor='val_accuracy', patience=6, restore_best_weights=True, verbose=1)
reduce_lr_cb = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-7, verbose=1)
callbacks = [checkpoint_cb, earlystop_cb, reduce_lr_cb]


# ---- TRAIN: head ----
print("Starting head training...")
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS,
    class_weight=class_weight,
    callbacks=callbacks
)


# ---- FINE-TUNING ----
if FINE_TUNE:
    print("Starting fine-tuning stage...")
    # Unfreeze from FINE_TUNE_AT layer in base_model
    base_model.trainable = True
    for layer in base_model.layers[:FINE_TUNE_AT]:
        layer.trainable = False

    # Recompile with a lower learning rate
    model.compile(
        optimizer=Adam(learning_rate=1e-5),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    fine_history = model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=FINE_TUNE_EPOCHS,
        class_weight=class_weight,
        callbacks=callbacks
    )


# ---- SAVE FINAL ----
final_path = os.path.join(MODEL_DIR, "tomato_disease_model.h5")
model.save(final_path)
print(f"Final model saved to: {final_path}")

# Save training history (combined)
try:
    hist = {}
    hist.update(history.history)
    if FINE_TUNE:
        # prefix fine-tune metrics to keep simple, or overwrite with last values
        for k, v in fine_history.history.items():
            hist.setdefault(k, []).extend(v)
    hist_path = os.path.join(MODEL_DIR, "training_history.json")
    with open(hist_path, "w", encoding="utf-8") as fh:
        json.dump(hist, fh, indent=2)
    print(f"Saved training history to {hist_path}")
except Exception as e:
    print("Could not save history:", e)