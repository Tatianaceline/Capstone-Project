# Hospital Stay Duration Prediction Project
## Overview
The goal of this project is to build a predictive model that identifies patients at high risk of hospital readmission.

## Table of Contents
1. Overview
2. Project Goals
3. Dataset
4. Modeling Approach
5. Evaluation Metrics
6. Results
7. Conclusion
8. Future Work
9. Contributors

## Project Goals
To create a model that predicts the risk of a patient being readmitted back into hospital based on key health indicators.

### Impact
This model will enable healthcare providers to;
Optimize resource allocation and bed management.
Improve staff scheduling for better patient outcomes.
Enhance patient satisfaction by reducing delays and ensuring availability of resources.

## Dataset
The dataset used for this project includes various features related to patients and their hospital stays, such as:

patient_nbr: Unique patient identifier
gender: Patient gender
age: Age group of the patient
weight: Patient weight (if recorded)
time_in_hospital: Actual length of stay (target variable)
medical_specialty: Specialty of the primary care provider
num_lab_procedures: Number of lab tests performed
num_procedures: Number of procedures during the stay
num_medications: Number of medications prescribed
number_outpatient: Previous outpatient visits
number_emergency: Emergency visits
number_inpatient: Prior inpatient admissions
number_diagnoses: Number of diagnoses
diabetesMed: Indicator if diabetes medication was prescribed
readmitted: Indicator if the patient was readmitted (used for classification tasks)
Data cleaning and preprocessing steps included handling missing values, encoding categorical variables, and scaling features as needed for optimal model performance.

## Modeling Approach
We explored various machine learning models, including:

Random Forest Regressor
Gradient Boosting Regressor
XGBoost Regressor
LightGBM Regressor
Each model was tuned to find the optimal hyperparameters, and feature engineering techniques were applied to improve accuracy and model interpretability.

## Evaluation Metrics
The model's performance was evaluated based on:

Mean Squared Error (MSE): Measures the average squared difference between predicted and actual values.
Root Mean Squared Error (RMSE): Provides an interpretable error value by taking the square root of MSE.
Prediction Accuracy: Estimated based on the RMSE as a percentage of the actual value range to gauge overall performance.

## Results
The final model achieved:

MSE: 16.62
RMSE: 4.08
Prediction Accuracy: 86.4%
These metrics indicate a reliable model performance, allowing us to predict hospital stay duration with reasonable accuracy. This insight can significantly impact operational efficiency in healthcare facilities.

## Conclusion
Our project aimed to predict hospital stay duration, which can help healthcare providers better allocate resources and improve patient care. Using advanced modeling techniques, we achieved predictions with an accuracy of around 86%, meaning our model can reliably anticipate average hospital stay lengths. This insight allows hospitals to plan staffing, bed occupancy, and supply needs more effectively. Future refinements could make these predictions even more accurate, ultimately supporting better operational efficiency and enhancing the patient experience.

## Future Work
Feature Engineering: Further refinement of features, including interaction terms and feature selection, could help improve model accuracy.
Alternative Models: Testing additional models such as neural networks for deeper insights and possibly higher accuracy.
Real-Time Prediction: Developing a deployment pipeline for integrating the model with hospital management systems to provide real-time predictions.
