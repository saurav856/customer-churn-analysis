import os
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Churn Predictor", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "telco.csv")

# ── Train model once ──────────────────────────────────────────────────────────
@st.cache_resource
def train_model():
    df = pd.read_csv(DATA_PATH)
    df['TotalCharges'] = df['TotalCharges'].replace(' ', float('nan'))
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna(subset=['TotalCharges'])
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    features = ["tenure", "MonthlyCharges", "TotalCharges",
                "Contract", "PaymentMethod", "InternetService",
                "SeniorCitizen", "PaperlessBilling"]

    df = df[features + ["Churn"]].dropna()

    encoders = {}
    cat_cols = ["Contract", "PaymentMethod", "InternetService", "PaperlessBilling"]
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    X = df[features]
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    return model, encoders, features, acc

model, encoders, features, accuracy = train_model()

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("📡 Telecom Churn Predictor")
st.caption(f"Model accuracy: **{accuracy:.1%}** (Random Forest on IBM Telco dataset)")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Details")
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 120.0, 65.0, step=0.5)
    total_charges = st.number_input("Total Charges ($)", 0.0, 9000.0, monthly_charges * tenure, step=10.0)
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])

with col2:
    st.subheader("Account Info")
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

st.divider()

# ── Predict ───────────────────────────────────────────────────────────────────
if st.button("🔍 Predict Churn Risk", use_container_width=True, type="primary"):
    input_dict = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Contract": encoders["Contract"].transform([contract])[0],
        "PaymentMethod": encoders["PaymentMethod"].transform([payment])[0],
        "InternetService": encoders["InternetService"].transform([internet])[0],
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "PaperlessBilling": encoders["PaperlessBilling"].transform([paperless])[0],
    }

    input_df = pd.DataFrame([input_dict])[features]
    prob = model.predict_proba(input_df)[0][1]
    label = model.predict(input_df)[0]

    st.subheader("Prediction Result")

    if prob >= 0.6:
        st.error(f"**High Churn Risk** — {prob:.1%} probability of churning")
        st.markdown("""
        **Recommended Actions:**
        - Offer a discounted annual or two-year contract upgrade
        - Incentivize switching to automatic payment (bank transfer or credit card)
        - Assign a retention specialist for proactive outreach
        """)
    elif prob >= 0.35:
        st.warning(f"**Moderate Churn Risk** — {prob:.1%} probability of churning")
        st.markdown("""
        **Recommended Actions:**
        - Send a loyalty offer or bundle discount
        - Check service quality (especially if on Fiber optic)
        - Consider a survey to capture dissatisfaction signals
        """)
    else:
        st.success(f"**Low Churn Risk** — {prob:.1%} probability of churning")
        st.markdown("This customer appears stable. Continue standard engagement.")

    # Feature importance bar
    st.subheader("What's driving this prediction?")
    importances = model.feature_importances_
    feat_df = pd.DataFrame({
        "Feature": features,
        "Importance": importances
    }).sort_values("Importance", ascending=False)

    st.bar_chart(feat_df.set_index("Feature")["Importance"])