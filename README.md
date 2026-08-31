# HOMNIQ-AI-House-Price-Prediction
#Live DEMO: https://github.com/ShizaEman/HOMNIQ-AI-House-Price-Prediction.git
## 📌 Project Overview

HOMNIQ AI is an end-to-end Machine Learning project developed to predict house prices using property-related features and regression algorithms.

The project focuses on understanding the complete Machine Learning workflow — from data preparation and exploratory analysis to model training, evaluation, cross-validation, hyperparameter tuning, and final model selection.

## 🎯 Project Objective

The main objective of this project is to build a reliable regression model that can estimate the price of a house based on its characteristics.

The model uses the following features:

- Overall Quality
- Living Area
- Garage Capacity
- Basement Area
- Year Built
- Full Bathrooms
- Number of Bedrooms
- Lot Area

## 🔄 Machine Learning Workflow
Dataset
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Cross-Validation
   ↓
Hyperparameter Tuning
   ↓
Model Comparison
   ↓
Final Model Selection
   ↓
House Price Prediction
🤖 Regression Models

Four regression algorithms were implemented and compared:

Linear Regression
Decision Tree Regression
Random Forest Regression
Gradient Boosting Regression
📊 Model Evaluation

The models were evaluated using:

MAE — Mean Absolute Error
MSE — Mean Squared Error
RMSE — Root Mean Squared Error
R² Score
Final Model Results
Model	MAE	RMSE	Testing R²
Linear Regression	10,431.66	12,505.46	0.972437
Tuned Gradient Boosting	13,084.38	16,368.98	0.952775
Tuned Random Forest	21,414.52	27,405.67	0.867624
Tuned Decision Tree	33,382.12	40,847.69	0.705922
🏆 Final Model

After comparing the models, Linear Regression was selected as the final model.

It achieved:

Testing R² Score: 0.972437

This means the final model explained approximately 97.24% of the variation in the test-set house prices.

The final model also achieved the lowest MAE and RMSE among the evaluated models.

🔬 Cross-Validation

Five-fold cross-validation was performed to check whether the models maintained consistent performance across different subsets of the training data.

This helped evaluate model reliability beyond a single train-test split.

⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed for the tree-based models to find better parameter combinations.

Decision Tree
max_depth = 5
min_samples_leaf = 2
min_samples_split = 5
Random Forest
max_depth = 20
min_samples_leaf = 1
min_samples_split = 2
n_estimators = 100
Gradient Boosting
learning_rate = 0.1
max_depth = 2
min_samples_leaf = 2
min_samples_split = 2
n_estimators = 200
🧠 Key Machine Learning Concepts Practiced

This project helped implement and understand:

Regression
Feature selection
Train-test splitting
Model evaluation
MAE, MSE and RMSE
R² Score
Cross-validation
K-Fold validation
Hyperparameter tuning
Model comparison
Overfitting and underfitting
Ensemble regression methods
Final model selection
🖥️ Prediction Interface

The trained model is integrated into a Streamlit interface called HOMNIQ AI, where users can enter property characteristics and receive an estimated house price.

The interface is designed to work across:

Desktop
Laptop
Tablet
Mobile
📁 Repository Structure
HOMNIQ-AI-House-Price-Prediction/
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
└── README.md
▶️ Run the Project Locally

Install the required libraries:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py
🚀 Project Outcome

This project demonstrates an end-to-end implementation of a supervised Machine Learning regression problem, including model development, evaluation, validation, optimization, comparison, and deployment.

👩‍💻 Developer

Shiza Eman

BS Artificial Intelligence


