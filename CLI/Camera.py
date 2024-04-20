import os
import cv2
import numpy as np
from PIL import Image, ImageOps  # Install pillow instead of PIL
from keras.models import load_model
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
#load module
print("Loading Camera Module")
import tensorflow as tf
model = load_model("keras-tm.h5", compile=False)

print("Model loaded")
# Load the labels
class_names = open("labels.txt", "r").readlines()

# Function to process a saved image with the model
def process_saved_image(image_path):
    # Open the image using Pillow
    image = Image.open(image_path).convert("RGB")

    # Resize and crop the image to fit the input shape required by the model
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Convert the image to a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Create an array of the right shape to feed into the model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Predict using the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    # Print prediction and confidence score
    pclass = class_name[2:]
    
    return pclass, confidence_score
   


def take_photo(camera_index=0, file_name='photo.jpg'):
    # Initialize camera
    camera = cv2.VideoCapture(camera_index)
    
    # Check if the camera is opened successfully
    if not camera.isOpened():
        print("Error: Unable to access the camera.")
        return
    
    # Capture a frame
    ret, frame = camera.read()
    
    if not ret:
        print("Error: Unable to capture frame.")
        camera.release()
        return
    
    # Save the frame as an image in the specified directory
    directory = ".\\users\\Current_User"  # Path to the directory
    file_path = os.path.join(directory, file_name)
    cv2.imwrite(file_path, frame)
    
    # Release the camera
    camera.release()
    print(f"Photo saved as {file_path}")

    

# Take photo using default camera (index 0) and save it in the specified directory
def list_camera_devices():
    # Try accessing camera devices until no more devices are found
    index = 0
    while True:
        camera = cv2.VideoCapture(index)
        if not camera.isOpened():
            break
        else:
            print(f"Camera {index}: Available")
            camera.release()
        index += 1

# List available camera devices
print("Camera Processing Module Sucess")



# Name of the saved image

