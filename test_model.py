import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

MODEL_PATH = "saved_models/tomato_disease_model.h5"
IMG_PATH = "sample.jpg"   # put an image here

labels = [
    'Bacterial_spot',
    'Early_blight',
    'Late_blight',
    'Leaf_Mold',
    'Septoria_leaf_spot',
    'Spider_mites_Two_spotted_spider_mite',
    'Target_Spot',
    'Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato_mosaic_virus',
    'healthy'
]

model = tf.keras.models.load_model(MODEL_PATH)

img = image.load_img(IMG_PATH, target_size=(224,224))
x = image.img_to_array(img)/255
x = np.expand_dims(x, axis=0)

pred = model.predict(x)
idx = np.argmax(pred)

print("Predicted class:", labels[idx])
print("Confidence:", pred[0][idx])
