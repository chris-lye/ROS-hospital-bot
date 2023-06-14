# CS470 Introduction to Artificial Intelligence
## KAIST Spring 2023
---
## Team S04
## Sterile Instrument Transporter (SIT)

### Objectives
1. To develop Computer Vision capable of accurately detecting thorough sterilization, characterized by the following functionalities:

  * the ability to detect the presence of a strip with the correct shade of dark green on the External Indicator 
  * the ability to detect the presence of a complete black bar on the Internal Indicator

2. To develop Computer Vision capable of classifying medical instruments, characterized by the following functionality:
  * the ability to classify between scissors, nail clippers, ear picks

---

## Notes
Please run the code on the Raspberry Pi attached to the Turtlebot.

## Anomaly Detection
Anomaly detection was used to identify whether an object in the image was different from the rest of the dataset, which in this case was the dataset of images of the peel pouches.

The anomaly detection model has been pre-trained and saved into ```anomaly_detection.pickle```. Run ```anomaly_detection.py``` to test the model.

## Object Detection
Object detection was used to identify if the peel pouches were sterilised, as well as the contents of the peel pouches. The object detection model has been pre-trained based on the aforementioned dataset, which we annotated by labelling manually. Run ```object_detection.py``` to test the model.