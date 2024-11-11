# Predictive Model for Patient Readmission

## Overview
Patient readmission is a critical issue in healthcare, indicating potential deficiencies in patient care and leading to significant costs. This project focuses on developing a predictive model to identify diabetic patients at high risk of readmission using advanced machine learning techniques.

## Objective
The primary goal of this project is to create a model that can effectively predict patient readmission by analyzing structured data. By leveraging machine learning algorithms, we aim to enhance patient outcomes and reduce unnecessary hospital visits.
This model will enable healthcare providers to;
  - Optimize resource allocation and bed management.
  - Improve staff scheduling for better patient outcomes.
  - Enhance patient satisfaction by reducing delays and ensuring availability of resources.


## Technologies Used
- Baseline Models: Random Forest,Logistic Regression,XG Boost Regressor etc for performance comparison.

## Dataset
The project utilizes the MIMIC-III synthetic diabetic dataset, which contains a wealth of information which include:
- Structured Data: Demographics, lab results, etc.

## Modeling Approach
We explored various machine learning models, including:

Random Forest Regressor
Gradient Boosting Regressor
XGBoost Regressor
LightGBM Regressor
Each model was tuned to find the optimal hyperparameters, and feature engineering techniques were applied to improve accuracy and model interpretability.


## Installation Instructions
1. Clone the Repository: 
   ```bash
   git clone <repository-url>
   ```
2. Set Up the Environment:
   - Make sure you have Python installed.
   - Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```
3. Download the Dataset: 
   - Obtain the MIMIC-III synthetic diabetic dataset and place it in the appropriate directory.

## Research Plan
1. Data Exploration:
   - Analyze the MIMIC-III synthetic diabetic dataset to understand its structure and contents.

2. Model Development:
   - Build a model for sequential data analysis and compare its effectiveness against Random Forest and Logistic Regression.

3. Evaluation:
   - Assess model performance using predictive accuracy and implement dropout techniques to mitigate overfitting.

## Contributors
- [Gilead Gad]
- [Kamal Ali]
- [Tatiana Temba]
- [Graffin Kiprotich]
- [Simon Muema]

## License
This project is licensed under the MIT License. Please see the LICENSE file for more details.

---

Feel free to modify any sections as needed or ask for additional information!
