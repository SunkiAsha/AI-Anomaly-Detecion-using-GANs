# AI-Anomaly-Detecion-using-GANs


1. Importing the packages
2. Exploring the dataset 
	- IoT-23 dataset
	- NSL - KDD
	- UNSW-NB15
3. Data processing
	- pandas dataframe
	- Keras Dataframe
	- Dropping unwanted column

4. Visualization using seaborn & matplotlib
5. Label Encoding using LabelEncoder
6. Feature Selection 
	- SelectPercentile using Mutual Info Classify
7. Splitting the data to train and test for Deep LEarning and X and y for ML
8. Building the model

	- CNN
	- DNN
	- LSTM
	- CNN-G
	- DNN-G
	- LSTM-G
	- SVM
	- Decision Tree
	- Voting Classifier 
	- Stacking CLassifier

9. Training and Building the model



Flask Framework
----------------

 
10. Flask Framework with Sqlite for signup and signin
11. Importing the packages
12. User gives input as Feature Values 
13. The given input is preprocessed for prediction
14. Trained model is used for prediction
15. Final outcome is displayed through frontend

DAtaset:
- IoT-23 dataset : https://www.kaggle.com/code/dhoogla/nf-ton-iot-00-cleaning/input

- NSL - KDD : 
https://www.kaggle.com/datasets/kaggleprollc/nsl-kdd99-dataset

- UNSW-NB15 : 
https://github.com/grimloc-aduque/Standard-Latent-Space-Dimension-For-Network-Intrusion-Detection-Systems-Datasets/tree/main/datasets

Extension
----------

In the base paper the author mentioned to use different  Dataset for analysis with Deep learning and Machine Learning  models, in which G-CNN got 90% of accuracy
As an extension we applied an ensemble method  combining the predictions of multiple individual models to produce a more robust and accurate final prediction.
However, we can further enhance the performance by exploring other ensemble techniques such as Voting Classifier and Stacking Classifier got 100% of accuracy 
As an extension we can build the front end using the flask framework for user testing and with user authentication.
