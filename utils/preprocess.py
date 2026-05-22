import cv2
import numpy as np

def preprocess_image(image_path):

    # Read image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize image to 28x28
    image = cv2.resize(image, (28, 28))

    # Invert image colors
    image = 255 - image

    # Normalize image
    image = image / 255.0

    # Reshape for CNN
    image = image.reshape(1, 28, 28, 1)

    return image