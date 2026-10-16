# 🚢 Titanic Survival Prediction

An end-to-end Machine Learning project that predicts passenger survival on the Titanic with 80%+ accuracy, deployed as an interactive Streamlit web app.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-orange)](https://scikit-learn.org)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://titanic-survival-prediction-67loo6y5ezc7uxgsgnyfmx.streamlit.app/)

🔗 Live Demo
**[https://titanic-survival-prediction-67loo6y5ezc7uxgsgnyfmx.streamlit.app/](https://titanic-survival-prediction-67loo6y5ezc7uxgsgnyfmx.streamlit.app/)**

---

### 📌 Overview
The sinking of the Titanic is one of history's most infamous tragedies. While luck played a role, certain groups were statistically more likely to survive. This project answers: **"What sorts of people were more likely to survive?"**

I built a complete ML pipeline: from EDA and feature engineering to model training and deployment.

### 🎯 Problem Statement
Binary Classification: Predict `Survived` (0 = No, 1 = Yes) based on passenger attributes like Pclass, Sex, Age, Fare, etc.

### 📊 Dataset
- **Source:** Kaggle Titanic Competition
- **Rows:** 891 (train), 418 (test)
- **Features:** 12 columns including Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Cabin
- **Target:** Survived

### 🔍 Key EDA Insights
- **Sex was #1 predictor:** Female survival rate ~74% vs Male ~19%
- **Class matters:** 1st Class ~63% survival vs 3rd Class ~24%
- **Age:** Children <10 had highest survival rate
- **Fare:** Higher fare correlated with higher survival
- **Embarked:** Port C had slightly higher survival

### 🛠️ Workflow

#### 1. Data Preprocessing
- Filled missing `Age` with median (grouped by Title/Pclass for better accuracy)
- Filled missing `Embarked` with mode
- Dropped `Cabin` (77% missing) but engineered `Deck` feature from it
- Created `Title` from Name (Mr, Mrs, Miss, Master, Rare)
- Created `FamilySize = SibSp + Parch + 1` and `IsAlone`

#### 2. Feature Engineering
- Label Encoding: Sex
- One-Hot Encoding: Embarked, Title, Pclass
- Feature Scaling: StandardScaler for Age, Fare
- Train/Test Split: 80/20 with stratification

#### 3. Modeling
**Algorithm: Logistic Regression**
Why? Interpretable, handles binary classification well, and performed best after GridSearchCV tuning.

Other models tested: Random Forest, Decision Tree, KNN

Model                Accuracy   Precision   Recall   F1
Logistic Regression  81.5%      0.80        0.73     0.76
Random Forest        79.3%      0.78        0.71     0.74

Final model: **~82% accuracy on test set** with 5-fold CV.

### 📁 Project Structure

Titanic-Survival-Prediction/
├── app.py                           # Streamlit app (main)
├── Titanic_Dataset_Analysis.ipynb   # Full EDA + Modeling Notebook
├── titanic_model.pkl                # Saved model
├── requirements.txt
├── data/
│   ├── train.csv
│   └── test.csv
└── README.md


🚀 Run Locally
1. Clone: git clone https://github.com/phixzas/Titanic-Survival-Prediction.git
2. Go to folder: cd Titanic-Survival-Prediction
3. Install: pip install -r http://requirements.txt
4. Run app: streamlit run http://app.py

💻 Tech Stack
Languages: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
Deployment: Streamlit Cloud



💻 Tech Stack
- *Languages:* Python
- *Libraries:* Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- *Deployment:* Streamlit Cloud
- *Version Control:* Git & GitHub

🌟 Features of Live App
- Interactive sidebar for passenger details (Pclass, Sex, Age, Fare, etc.)
- Real-time survival prediction with probability
- Clean UI with survival insights
- Model explainability: Shows which features drove the prediction

📈 Future Improvements
- [ ] Add XGBoost / LightGBM comparison
- [ ] Add SHAP for model explainability
- [ ] Deploy with FastAPI + Docker
- [ ] Add model monitoring

👨‍💻 Author
*Felix / phixzas*
- GitHub: [@phixzas](https://github.com/phixzas)
- Live Project: [Titanic App](https://titanic-survival-prediction-67loo6y5ezc7uxgsgnyfmx.streamlit.app/)
- Portfolio ready for Data Science roles







👨‍💻 Author
Felix / phixzas
GitHub: https://github.com/phixzas
Live Project: https://titanic-survival-prediction-67loo6y5ezc7uxgsgnyfmx.streamlit.app/

---
This project is for educational and portfolio purposes.
