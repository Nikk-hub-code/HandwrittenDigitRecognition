from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import os

from utils.preprocess import preprocess_image

app = Flask(__name__)

# Load trained model
model = load_model("models/digit_model.h5")

# Upload folder
UPLOAD_FOLDER = "app/static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    # Save uploaded image
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Preprocess image
    processed_image = preprocess_image(filepath)

    # Predict digit
    prediction = model.predict(processed_image)

    predicted_digit = np.argmax(prediction)

    return render_template(
        "index.html",
        prediction=predicted_digit,
        image_path=filepath
    )

if __name__ == "__main__":
    app.run(debug=True)