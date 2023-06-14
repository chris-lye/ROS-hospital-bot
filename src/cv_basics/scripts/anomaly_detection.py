import cv2  # OpenCV library
import pickle
import os
import glob


# Colour Histograms for Characterisation of Images
def quantify_image(image, bins=(4, 6, 3)):
    # compute a 3D color histogram over the image and normalize it
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    # return the histogram
    return hist


pickle_in = open(os.getcwd() + "/anomaly_detection.pickle", "rb")
model = pickle.load()

test_data_paths = glob.glob("/home/ubuntu/s4/catkin_ws/src/cv_basics" + "/*.png")
# use the anomaly detector model and extracted features to determine
# if the example image is an anomaly or not
results = []
for i in range(len(test_data_paths)):
    input_image_path = test_data_paths[i]
    image = cv2.imread(input_image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    features = quantify_image(hsv, bins=(3, 3, 3))
    preds = model.predict([features])[0]
    label = test_data_paths[i].split("/")[-1] + " : "
    result = "anomaly" if preds == -1 else "normal"
    label += result
    color = (0, 0, 255) if preds == -1 else (0, 255, 0)

    # draw the predicted label text on the original image
    cv2.putText(image, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
    # display the image
    cv2_imshow(image)

    results.append({"label": result, "path": test_data_paths[i]})
    print("label: " + result, "path: " + test_data_paths[i])
