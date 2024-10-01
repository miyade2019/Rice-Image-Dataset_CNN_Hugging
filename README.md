
# 🍚 Rice Image Classification using CNN and HuggingFace
This repository contains a project focused on classifying different types of rice grains using Convolutional Neural Networks (CNNs). The model uses TensorFlow and leverages HuggingFace tools for fine-tuning and deployment.

## 🚀 Project Overview
This project aims to classify different varieties of rice from images in the Rice Image Dataset. Image classification is crucial for quality control in agriculture, and accurate models can help farmers and producers ensure the quality of their products.

## ✨ Key Features:
Dataset: Rice Image Dataset contains high-quality images of different rice varieties.
Modeling Approach: A CNN is built from scratch and fine-tuned for effective rice classification.
Transfer Learning with HuggingFace: Utilized HuggingFace tools to improve model performance and enable easy deployment.
## 📁 Dataset
The dataset consists of images of several varieties of rice. Each image represents a particular type of rice grain, and the dataset is used to train the model to distinguish between these types.(Dataset)[https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset ]

Classes: Basmati, Jasmine, Arborio, etc.
Number of Images: 12,000+
Image Size: 256x256 pixels
## 📈 Approach
Data Preprocessing: The dataset was preprocessed using image augmentation techniques such as rotations, zooms, and flips to make the model more robust.
Model Building:
Created a CNN from scratch using TensorFlow to learn distinctive features of each type of rice.
Applied transfer learning using pretrained models available through HuggingFace to enhance performance.
Training & Evaluation: The model was trained on 80% of the dataset, with 20% used for validation to monitor overfitting.
## 🛠️ Tools & Libraries
Python: The primary language used.
TensorFlow & Keras: For building and training the CNN model.
HuggingFace Transformers: For fine-tuning and deployment.
OpenCV: For image processing tasks.
Matplotlib & Seaborn: For visualizing results and metrics.
## 🎯 Results
Accuracy: The CNN achieved an accuracy of 98% on the test set, showcasing its effectiveness in distinguishing rice varieties.
Confusion Matrix: The confusion matrix and classification report are available to show the model's performance in detail.
