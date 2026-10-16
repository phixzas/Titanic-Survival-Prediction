import streamlit as st 
import pickle
import pandas as pd
import os

base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'model.pkl')
model = pickle.load(open(model_path, 'rb'))


st.title("Titanic Surviver")
st.write("Professional Surviver Prediction")

st.markdown(
    """
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
        width: 220px;
        height: 52px;
        font-size: 22px;
        font-weight: 700;
        border-radius: 12px;
        background: linear-gradient(90deg, #1f77b4 0%, #4caf50 100%);
        color: white;
        border: none;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
    }
    .stSuccess, .stError {
        font-size: 1.25rem;
        padding: 1rem 1.2rem;
        border-radius: 0.75rem;
    }
    div[data-testid="stNumberInputRoot"] {
        position: relative;
    }
    div[data-testid="stNumberInputRoot"] > label {
        display: block;
    }
    div[data-testid="stNumberInputRoot"] input {
        padding-left: 26px;
    }
    div[data-testid="stNumberInputRoot"]::before {
        content: "$";
        position: absolute;
        left: 12px;
        top: 52%;
        transform: translateY(-50%);
        font-weight: 700;
        color: #4b5563;
        z-index: 1;
        pointer-events: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
pclass = st.selectbox("pclass", ["Select class in the ship", "1", "2", "3"])
gender = st.selectbox("Gender", ["Select sex of the passenger", "Male", "Female"])
age = st.number_input("Age", min_value=0.0, value=None, step=1.0, placeholder="Input the age of passenger")
sibsp = st.selectbox("SibSp", ["Select SibSp in the ship", "0", "1", "2", "3", "4", "5", "6", "7", "8"])
parch = st.selectbox("Parch", ["Select Parch in the ship", "0", "1", "2", "3", "4", "5", "6"])
fare = st.number_input("Fare", min_value=0.0, value=None, step=1.0, placeholder="Input the fare")
embarked = st.selectbox("Embarked", ["Select Embarked", "S", "Q", "C"])

if st.button("Predict"):
    required_fields = {
        "Passenger class": pclass,
        "Gender": gender,
        "SibSp": sibsp,
        "Parch": parch,
        "Embarked": embarked,
    }

    for label, value in required_fields.items():
        if value.startswith("Select"):
            st.error(f"Please choose an option for: {label}.")
            st.stop()

    if age is None or fare is None:
        st.error("Please enter both age and fare.")
        st.stop()

    sex_female = 1 if gender == "Female" else 0
    if embarked == "S":
        Embarked_S, Embarked_Q, Embarked_C = 1, 0, 0
    elif embarked == "Q":
        Embarked_Q, Embarked_S, Embarked_C = 1, 0, 0
    else:
        Embarked_C, Embarked_Q, Embarked_S = 1, 0, 0

    features = pd.DataFrame(
        [[float(pclass), sex_female, age, float(sibsp), float(parch), fare,
          Embarked_C, Embarked_Q, Embarked_S]],
        columns=[
            "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare",
            "Embarked_C", "Embarked_Q", "Embarked_S",
        ],
    )

    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.success(f"✅ The person Survived! Confidence: {proba*100:.1f}%")
    else:
        st.error(f"❌ The person did not Survived! Confidence: {(1-proba)*100:.1f}%")