# Import the necessary packages
from imutils import paths
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import argparse
import pickle
import os
import glob
from google.colab.patches import cv2_imshow


# Colour Histograms for Characterisation of Images
def quantify_image(image, bins=(4, 6, 3)):
    # compute a 3D color histogram over the image and normalize it
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    # return the histogram
    return hist


# Load dataset
def load_dataset(datasetPath, bins):
    # grab the paths to all images in our dataset directory, then
    # initialize our lists of images
    imagePaths = list(paths.list_images(datasetPath))
    print(imagePaths)
    print(datasetPath)
    data = []
    # loop over the image paths
    for imagePath in imagePaths:
        # load the image and convert it to the HSV color space
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # quantify the image and update the data list
        features = quantify_image(image, bins)
        data.append(features)
    # return our data list
    return data


# dataset paths (to replace with your own)
nail_clippers_sterilised = "/content/gdrive/MyDrive/SUTD/Term 6 KAIST/CS470 Introduction to Artificial Intelligence/FRIGGIN ROBOT/Dataset/new dataset/nail-clippers1/sterilized/"
scissors_sterilised = "/content/gdrive/MyDrive/SUTD/Term 6 KAIST/CS470 Introduction to Artificial Intelligence/FRIGGIN ROBOT/Dataset/new dataset/scissors1/sterilized/"
nail_clippers_unsterilised = "/content/gdrive/MyDrive/SUTD/Term 6 KAIST/CS470 Introduction to Artificial Intelligence/FRIGGIN ROBOT/Dataset/new dataset/nail-clippers1/unsterilized/"
scissors_unsterilised = "/content/gdrive/MyDrive/SUTD/Term 6 KAIST/CS470 Introduction to Artificial Intelligence/FRIGGIN ROBOT/Dataset/new dataset/scissors/unsterilized/"
none_sterilised = "/content/gdrive/MyDrive/SUTD/Term 6 KAIST/CS470 Introduction to Artificial Intelligence/FRIGGIN ROBOT/Dataset/new dataset/none/sterilized"
none_unsterilised = "/content/gdrive/MyDrive/SUTD/Term 6 KAIST/CS470 Introduction to Artificial Intelligence/FRIGGIN ROBOT/Dataset/new dataset/none/unsterilized"

# load and qutantify our image dataset
print("[INFO] preparing NC_S dataset...")
nail_clippers_sterilised_images = load_dataset(nail_clippers_sterilised, bins=(3, 3, 3))
print("[INFO] preparing S_S dataset...")
scissors_sterilised_images = load_dataset(scissors_sterilised, bins=(3, 3, 3))
print("[INFO] preparing NC_US dataset...")
nail_clippers_unsterilised_images = load_dataset(
    nail_clippers_unsterilised, bins=(3, 3, 3)
)
print("[INFO] preparing S_US dataset...")
scissors_unsterilised_images = load_dataset(scissors_unsterilised, bins=(3, 3, 3))
print("[INFO] preparing NONE_S dataset...")
none_sterilised_images = load_dataset(none_sterilised, bins=(3, 3, 3))
print("[INFO] preparing NONE_US dataset...")
none_unsterilised_images = load_dataset(none_unsterilised, bins=(3, 3, 3))

# training data = sterilised images
train_data = (
    nail_clippers_sterilised_images
    + scissors_sterilised_images
    + nail_clippers_unsterilised_images
    + scissors_unsterilised_images
    + none_sterilised_images
    + none_unsterilised_images
)
# Transform to Numpy array
train_data = np.array(train_data)

# train the anomaly detection model
print("[INFO] fitting anomaly detection model...")
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
model.fit(train_data)

# serialize the anomaly detection model to disk
output_path = "/content/gdrive/MyDrive/SUTD/Term 6 KAIST/CS470 Introduction to Artificial Intelligence/FRIGGIN ROBOT/CV_model"
pickle_out = open(output_path + "/anomaly_detection.pickle", "wb")
pickle.dump(model, pickle_out)
pickle_out.close()
