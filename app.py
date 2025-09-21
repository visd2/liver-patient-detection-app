import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

# Load model & scaler
model = joblib.load('liver_model.pkl')
scaler = joblib.load('liver_scaler.pkl')

# Page config
st.set_page_config(
    page_title="Liver Disease Predictor",
    page_icon="🩺",
    layout="wide"
)

# Sidebar
st.sidebar.title("🩺 Liver Disease Prediction App")
st.sidebar.markdown("""
This app predicts liver disease based on patient data.
- Fill the form with patient details
- Click Predict
- Get result with risk probability
""")

# Input section in columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 1, 120, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tb = st.number_input("Total Bilirubin", min_value=0.0, value=1.0)
    db = st.number_input("Direct Bilirubin", min_value=0.0, value=0.5)
    aps = st.number_input("Alkaline Phosphotase", min_value=0.0, value=150.0)

with col2:
    alt = st.number_input("Alamine Aminotransferase (ALT)", min_value=0.0, value=30.0)
    ast = st.number_input("Aspartate Aminotransferase (AST)", min_value=0.0, value=30.0)
    tp = st.number_input("Total Proteins", min_value=0.0, value=6.5)
    albumin = st.number_input("Albumin", min_value=0.0, value=3.5)
    agr = st.number_input("Albumin/Globulin Ratio", min_value=0.0, value=1.0)

# Predict button
if st.button("Predict"):
    gender_val = 1 if gender == "Male" else 0
    features = np.array([age, gender_val, tb, db, aps, alt, ast, tp, albumin, agr]).reshape(1, -1)
    features_scaled = scaler.transform(features)

    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0,1]

    # Risk meter using plotly gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob*100,
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "red" if pred==1 else "green"}},
        title={'text': "Liver Disease Risk (%)"}
    ))

    st.plotly_chart(fig, use_container_width=True)

    # Colored message
    if pred == 1:
        st.markdown(f"<h2 style='color:red;'>⚠️ Liver Disease Detected! Probability: {prob:.2f}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='color:green;'>✅ No Liver Disease Detected! Probability: {1-prob:.2f}</h2>", unsafe_allow_html=True)
