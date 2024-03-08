import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the first model for peppermint detection
peppermint_model = keras.models.load_model(
    r'peppermint.h5')

# Load the second model for health prediction
health_model = keras.models.load_model(
    r'Peppermint_Classes_Premodel.h5')


def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.vgg16.preprocess_input(
        img_array)  # Use VGG16 preprocessing
    return img_array


def predict_peppermint(img_path):
    img_array = preprocess_image(img_path)
    prediction = peppermint_model.predict(img_array)
    return prediction


def predict_health(img_path):
    img_array = preprocess_image(img_path)
    prediction = health_model.predict(img_array)
    return prediction


def main(image_path):
    peppermint_prediction = predict_peppermint(image_path)

    # Print the raw peppermint prediction
    # print("Raw Peppermint Prediction:", peppermint_prediction)

    # Print the predicted class index based on the highest probability
    predicted_class = np.argmax(peppermint_prediction)
    # print("Predicted Peppermint Class:", predicted_class)

    # Assuming the output classes of the peppermint detection model are [0: Pudina, 1: Random Objects]
    if predicted_class == 0:
        health_prediction = predict_health(image_path)

        # Print the raw health prediction
        # print("Raw Health Prediction:", health_prediction)

        # Extract probabilities for each class
        health_probabilities = health_prediction[0]

        # Assuming the output classes of the health prediction model are [0: Dried, 1: Fresh, 2: Spoiled, 3: Sunlight]
        # for i, prob in enumerate(health_probabilities):
        #     print(f"Probability for class {i}: {prob}")

        # Determine the predicted health class
        health_class = np.argmax(health_prediction)

        # print("Predicted Health Class:", health_class)

        if health_class == 0:
            print("Peppermint (Pudina) detected, and it is Dried.")
        elif health_class == 1:
            print("Peppermint (Pudina) detected, and it is Fresh.")
        elif health_class == 2:
            print("Peppermint (Pudina) detected, but it is Spoiled.")
    else:
        print("Error in peppermint prediction.")


# Example usage
image_path = r'D:\Git Projects\Peppermint-Identification-and-Classification-Model\Data\Apple Leaf Dataset\AlternariaBoltch_000000.jpg'
main(image_path)
