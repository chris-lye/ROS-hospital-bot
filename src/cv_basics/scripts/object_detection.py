import cv2 # OpenCV library
from roboflow import Roboflow

rf = Roboflow(api_key="EdMQQpIClNRzSt4WA4OW")
project = rf.workspace("cs470").project("object-detection-new-9bjba")
model = project.version(1).model

for i in range(len(test_data_paths)):
	input_image_path = test_data_paths[i]
	print(model.predict(input_image_path, confidence=40, overlap=30).json())
	# visualize prediction
	label = input_image_path.split('/')[-1]
	prediction_file_path = "prediction_" + result + "_" + label + ".jpg"
	model.predict(input_image_path, confidence=40, overlap=30).save(prediction_file_path)
		
	# display the image with bounding boxes
	cv2_imshow(cv2.imread(prediction_file_path))
