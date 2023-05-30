# yolov5_reduced_classes
An attempt to increase accuracy of the yolov5 model for a specific task by reducing the number of classes.

## Introduction
The aim of this project is to train yolov5 model on a custom dataset with reduced number of classes to achive an increase in accuracy.

The dataset used in this work is a filtered COCO dataset with 3 classes: Person, Pet (Cat+Dog), Vehicle (car+bus+truck).

## 1. Creating a custom dataset
To create a custom dataset dataset custom_dataset/filter.py is used with COCO labels file (json). Example: **python filter.py --input_json c:\users\you\annotations\instances_train2017.json --output_json c:\users\you\annotations\filtered.json --categories person dog cat**. Then, using custom_dataset/coco2yolo.ipynb, the filtered COCO format labels are converted into yolo format labels (json -> txt).

## 2. Training yolov5 model using custom dataset
