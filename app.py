import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

# Load dataset
df = pd.read_csv("titanic.csv")

# Drop unnecessary columns
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Encode categorical columns
sex_encoder = LabelEncoder()
embarked_encoder = LabelEncoder()

df["Sex"] = sex_encoder.fit_transform(df["Sex"])
df["Embarked"] = embarked_encoder.fit_transform(df["Embarked"])

# Features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = SVC(kernel="linear")
model.fit(X_train, y_train)

# Streamlit UI
st.title("Titanic Survival Prediction using SVM")

st.write("### Enter Passenger Details")

pclass = st.selectbox("Passenger Class", [1, 2, 3])

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

age = st.number_input("Age", min_value=0, max_value=100, value=25)

sibsp = st.number_input("Siblings/Spouses", min_value=0, max_value=10, value=0)

parch = st.number_input("Parents/Children", min_value=0, max_value=10, value=0)

fare = st.number_input("Fare", min_value=0.0, value=30.0)

embarked = st.selectbox("Embarked", ["C", "Q", "S"])
embarked = {"C": 0, "Q": 1, "S": 2}[embarked]

if st.button("Predict"):

    input_data = pd.DataFrame(
        [[pclass, sex, age, sibsp, parch, fare, embarked]],
        columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Passenger Survived")
    else:
        st.error("Passenger Did Not Survive")