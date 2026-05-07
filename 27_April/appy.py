
#streamlit UI
import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("iris.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌸 Iris Flower Prediction App")

st.write("Enter flower measurements below:")

sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")

if st.button("Predict"):
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction = model.predict(input_features)

    species = ["Setosa", "Versicolor", "Virginica"]

    st.success(f"🌿 Predicted Iris Species: **{species[prediction[0]]}**")
