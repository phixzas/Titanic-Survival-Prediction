# Titanic Survival Prediction using Machine Learning

## 📊 Project Overview

🚢 Titanic Dataset Analysis: This project predicts whether a passenger survived the Titanic disaster using machine learning. The workflow includes data cleaning, exploratory data analysis (EDA), feature engineering, model training, and model evaluation.

---

## Objective

To build a machine learning model that predicts passenger survival based on passenger information such as age, sex, passenger class, and fare.

---

## Dataset

- Source: Kaggle Titanic Dataset
- Total Rows: 891
- Total Columns: 12

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook


git clone https://github.com/Amolak001/Titanic-Dataset-Analysis.git
Install required packages:

pip install -r requirements.txt
Open the Jupyter Notebook:

jupyter notebook Titanic_Dataset_Analysis.ipynb
📊 Visualization Preview
---

## Data Preprocessing

- Filled missing Age values using the median
- Filled missing Embarked values using the mode
- Dropped the Cabin column because of many missing values
- Encoded categorical variables
- Split the data into training and testing datasets

---

## Exploratory Data Analysis

Key findings include:

- Female passengers had a higher survival rate than male passengers.
- First-class passengers survived more frequently than third-class passengers.
- Children had the highest survival rate.
- Passenger class had a significant impact on survival.

---

## Machine Learning Model

Algorithm used:

- Logistic Regression

---

## Model Performance

| Metric | Score |
|---------|------:|
| Accuracy | 81% |
| Precision | 79% |
| Recall | 74% |
| F1 Score | 76% |

---

## Conclusion

The Logistic Regression model achieved an accuracy of approximately 81%. This project demonstrates the complete machine learning workflow, from data preprocessing and exploratory data analysis to model training and evaluation.

---

## Author

Mayowa Philips Olusanjo
Github: https://github.com/phixzas
LinkedIn: www.linkedin.com/in/mayowa-philips-olusanjo-982663152
















