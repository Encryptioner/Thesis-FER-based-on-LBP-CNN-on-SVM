# Facial Expression Recognition Based on LBP and CNN : A Comparative Study Using SVM Classifier
# Graduation thesis work



Necessary code sources for Thesis work titled "Facial Expression Recognition Based on LBP and CNN : A Comparative Study Using SVM Classifier"

Language: Python
Course No: CSE 4000
Dept. of CSE, RUET

Author: Mir Mursalin Hossain
Roll: 133047

Supervisor: Prof. Dr. Md. Rabiul Islam


--------------------------------------


Here, Emotion labels are represented as:

0=Neutral, 1=Anger, 2=Disgust, 3=Fear, 4=Happiness, 5=Sadness, 6=Surprise


Image Datasets are:

CK+, JAFFE, KDEF, FER2013



# Step 1 & 2: Dataset Processing & Image pre-processing:


All the image dataset is transformed into grayscale. FER2013 is allready in grayscale of 48*48 images presented in CSV file. CK+ and KDEF dataset is resized into 256 ∗ 256. Facial image is detected, cropped and aligned using 68-point facial landmark. CK+, JAFFE and KDEF dataset is modified in the version of CSV file containing emotion label and flatten pixel value. So there are 256 ∗ 256 or 65536 pixel value and an emotion label is assigned per image of expression dataset.




-> CK+ dataset comes with 8 Emotion labels, FACs labels, Landmarks and Extended cohn-kanade images folder. For each individual there was number of facial expression but most of them have all facial expression image. Modified dataset was prepared manually by taking all facial expression image with right dedicated labels stored in Emotion labels folder. 


1. Face alignment: align_faces.py
2. Face Cropping: crop_faces.py
3. Image Resizing: resize_image_in_required_format.py
4. Creating CSV dataset: images_to_csv.py
5. Plot Dataset: data_labels_file.py, plot_dataset.py



-> JAFFE contains facial expression for 10 Japanese women by taking each expression 3 times. Though not all emotion labels have 30 image. Some emotion label contains less or more. 


1. Face alignment: align_faces.py
2. Face Cropping: crop_faces.py
3. Image Resizing: resize_image_in_required_format.py
4. Creating CSV dataset: images_to_csv.py
5. Plot Dataset: data_labels_file.py, plot_dataset.py



-> KDEF contains 4900 image. Only frontal image of 70 individuals is taken in modified dataset.


1. Face alignment: align_faces.py
2. Face Cropping: crop_faces.py
3. Image Resizing: resize_image_in_required_format.py
4. Creating CSV dataset: images_to_csv.py
5. Plot Dataset: data_labels_file.py, plot_dataset.py



-> FER2013comes as CSV file with emotion, pixels and Usage. In original datast label '0' represented 'anger' and so on. Thats why emotion label is changed so that in all our dataset each emotion label has one dedicated value. The Usage with ”Training” is taken as training dataset, usage ”PublicTest” is used as validation set and ”PrivateTest” is used as testing set. 


1. Modifying FER2013 Dataset emotion label: modifying_fer2013_emotion_label.py
2. CSV file to Image Dataset: cv_file_to_image_dataset.py
3. Face alignment: align_faces.py
4. Face Cropping: crop_faces.py
5. Image Resizing: resize_image_in_required_format.py
6. Creating CSV dataset: images_to_csv.py



# Step 3: Feature Extraction:


Face region is detected using 68-point facial landmark. Landmark vector of shape (68, 2) is saved for each dataset. For LBP feature of rotational invariant circular uniform LBP detecton (no of points, radius) = (24,8) is choosed. So feature length is a vector of size 26. As, radius 8 is good to capture necessary feature of large  scale. no of points 24 is efficient to train SVM in quick time. Other combination was also tried and no other gave significant better peformance than this.


Parameter of SVM is choosed using Grid Search applying on smaller dataset. Necessary Codes for these processes are below:


1. Finds LBP Histogram from given image: lbp1_localbinarypatterns.py
2. Sample dataset training to find best parameter: lbp1_training.py
3. Sample testing to find best parameter: lbp1_testing.py
4. Both Training and testing to find which parameter gives good result: lbp1_recognize.py


LBP feature vector and Facial Landmark vector is found by passing different image dataset in CSV format. Necessary Codes for these processes are below:

1. Select dataseet and output folder variable: parameters.py
2. Data loading function: data_loader.py
3. feature extraction and saving output feature vector: dataset_to_LBP_Landmark_Feature.py


Dataset is trained in CNN model. Input data of first fully connected layer is used as CNN feature to later train SVM classifier. CNN feature vector size is 128. This part is done using a kernel in kaggle.com. Necessary file are uploaded and then feature extraction is done. Necessary Codes for these processes are below:

1. FER-Landmarks-CNN-LBP-SVM on FER2013.txt
2. FER-Landmarks-CNN-LBP-SVM on KDEF.txt




# Step 4: Classification:


Both LBP and CNN feature vector is trained on Support Vector Machine of both linear and non-linear kernel. For non-linear kernel ’rbf’ was used. Accuracy with confusion matrix and classification report is showed to highlight the performance of both method. This part is done using same kernel in kaggle.com. LBP based SVM and CNN based SVM is trained on FER2013 dataset and KDEF dataset and then tested on various dataset. Necessary Codes for these processes are below:


1. FER-Landmarks-CNN-LBP-SVM on FER2013.txt
2. FER-Landmarks-CNN-LBP-SVM on KDEF.txt


-------------------------------------------



More details is discussed in thesis paper.
Kaggle Link: https://www.kaggle.com/ankur133047/kernels

