import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load model
model = tf.keras.models.load_model("giraffe_tiger_classifier.keras")

# Class names
class_names = ["Giraffe", "Tiger"]

st.title("🦒🐯 Giraffe vs Tiger Image Classifier")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    image = image.resize((150, 150))

    img_array = tf.keras.utils.img_to_array(image)

    # Don't divide by 255 because the model already rescales the image
    img_array = tf.expand_dims(img_array, 0)

    prediction = model.predict(img_array)

    score = tf.nn.softmax(prediction[0])

    st.write("### Prediction")
    st.success(class_names[np.argmax(score)])

    st.write(f"Confidence: {100*np.max(score):.2f}%")