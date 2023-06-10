# yolov5_reduced_classes
An attempt to increase accuracy of the yolov5 model for a specific task by reducing the number of classes.

## Introduction
The aim of this project is to train yolov5 model on a custom dataset with reduced number of classes to achive an increase in accuracy.

The dataset used in this work is a filtered COCO dataset with 3 classes: Person, Pet (Cat+Dog), Vehicle (car+bus+truck).

## 1. Creating a custom dataset
To create a custom dataset dataset custom_dataset/filter.py is used with COCO labels file (json). Example: **python filter.py --input_json c:\users\you\annotations\instances_train2017.json --output_json c:\users\you\annotations\filtered.json --categories person dog cat**. Then, using custom_dataset/coco2yolo.ipynb, the filtered COCO format labels are converted into yolo format labels (json -> txt).

## 2. Training yolov5 model using custom dataset
For training the yolov5 model a data config file must be created (dataset.yaml). Dataset config file is a file that defines 1) the dataset root directory path and relative paths to train / val / test image directories (or .txt files with image paths) and 2) a class names dictionary. After that the model yolov5n model was trained in 200 epochs.

## 3. Validation for custom trained and original models
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/000000035682_original.jpg)
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/000000035682_custom.jpg)

## 4. Detection comparison with the base model

In addition to the validation results, it would be beneficial to look at the detection examples and compare them to the results of the base model, image by image. As we compare the models using test images we can obeserve minor differences in most cases (slight change in confidence score and bounding box size and position). However, in some cases the custom model appears to have an advantage. 

When comparing detection results LEFT is base model RIGHT is custom model.
# Contrast 

The custom model seems to show better results compared to the base YOLOv5 in cases where the object doesn't stand out against the background. A good example for such case is a vehicle driver/passenger covered by the reflection of a window. With another complication in the form of dim lighting inside the vehicle, we get a hardly recognizable upper body silhouette. 
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/5037.jpg)
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/6040.jpg)

# Partial visibility
In cases where only part of an object is visible the custom model also shows promising results, it is especially apparent when the visible part is the upper body of a person or a pet. 
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/1251.jpg)
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/61108.jpg)
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/27696.jpg)
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/968.jpg)
Although there are cases where the base model performed better when the visible part is a lower part (for example when only legs are visible).
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/3553.jpg) 

# Crowd detection
This is, in my opinion, the most interesting result that came out during this experiment. 
In COCO dataset there are a many pictures of crowded places such as sporting events or popular public places. Using these cases the model seems to develop a "subclass" of a person class for cases where there are a lot of people close to each other.

![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/65798.jpg)
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/2343.jpg) 
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/72795.jpg)
![App Screenshot](https://raw.githubusercontent.com/AlexeyDzyubaP/yolov5_reduced_classes/main/screenshots/60886.jpg) 

In some cases we can see that this improvement alows the model to detect multiple people when detecting them one by one is nearly impossible (like a stand full of people watching a sport event shot from a long distance). This could prove to be quite usefull if only we could reliably separate the "crowd" detection instaces from a regular person detection instances. The solution might be to separate these 2 classes by the size of the bounding box. In most applications of a YOLO type model the objects are rarely shot from a close distance, therefore, the bounding box for a person-type object usually takes up no more than 10-20% of an image. Therefore, if we detect a person-type object with a bounding box for than a set percentage of an image we can relabel it as a crowd-type object. This method could futher be improved by comparing the largest bounding box with the others in the same image or by counting the number of others person-type objects inside the bounding box.

## 5. Conclusion 
