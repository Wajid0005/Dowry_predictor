import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

import joblib

# ================= CONFIG =================
st.set_page_config(
    page_title="Dahej Predictor (Educational)",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# ================= SESSION STATE =================
if "step" not in st.session_state:
    st.session_state.step = 0

if "responses" not in st.session_state:
    st.session_state.responses = {}

TOTAL_STEPS = 15

# ================= MAPPINGS (CRITICAL) =================
OCCUPATION_MAP = {
    "Private Job": "Private jobs",
    "Government Job": "Govt-jobs",
    "Business": "Business",
    "Freelancer": "Freelancer",
    "Self-employed": "Self-employed",
    "Unemployed": "Unemployed"
}

PERSONALITY_MAP = {
    "Chill": "Remo",
    "Ambi": "Ambi"
}

BACKGROUND_MAP = {
    "Urban": "U",
    "Rural": "R"
}

EDUCATION_MAP = {
    "No Formal Education": "Uneducated",
    "10th Pass": "12th Pass",
    "12th Pass": "Graduate",
    "Graduate": "Graduate",
    "Postgraduate+": "ITUS"
}

FAMILY_MAP = {
    "Joint": "Joint",
    "Nuclear": "Nuclear",
    "Living Alone": "Alone"
}

# ================= HELPERS =================
def next_step():
    st.session_state.step += 1
    st.rerun()

def prev_step():
    st.session_state.step = max(0, st.session_state.step - 1)
    st.rerun()

def progress_ui():
    st.progress(st.session_state.step / TOTAL_STEPS)
    st.caption(f"Step {st.session_state.step} / {TOTAL_STEPS}")

def card(title):
    st.markdown(
        f"""
        <div style="
            background:#ffffff;
            padding:30px;
            border-radius:14px;
            box-shadow:0 10px 30px rgba(0,0,0,0.12);
            margin-top:30px;
        ">
        <h3>{title}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= MAIN APP =================
card("Dahej Expectation Simulator (Educational Project)")

# ---------- STEP 0 ----------
if st.session_state.step == 0:
    st.session_state.responses["name"] = st.text_input("Your Name (optional)")

    if st.button("Start"):
        next_step()
    progress_ui()

# ---------- STEP 1 : OCCUPATION ----------
elif st.session_state.step == 1:
    card("Occupation")

    for k in OCCUPATION_MAP.keys():
        if st.button(k):
            st.session_state.responses["Occupation"] = OCCUPATION_MAP[k]
            next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 2 : INCOME ----------
elif st.session_state.step == 2:
    card("Yearly In-Hand Income (INR)")

    income = st.slider("Income", 0, 10_00_00_000, step=50_000)
    st.session_state.responses["Yearly_Inhand_Income_INR"] = float(income)

    if st.button("Next ➡"):
        next_step()
    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 3 : AGE ----------
elif st.session_state.step == 3:
    card("Age")

    age = st.number_input("Age", min_value=18, max_value=55)
    st.session_state.responses["Age"] = int(age)

    if st.button("Next ➡"):
        next_step()
    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 4 : POLITICAL ----------
elif st.session_state.step == 4:
    card("Political View (Simplified)")

    if st.button("Modi"):
        st.session_state.responses["Political_view"] = 1
        next_step()
    if st.button("Rahul"):
        st.session_state.responses["Political_view"] = 0
        next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 5 : HOUSE ----------
elif st.session_state.step == 5:
    card("Owns House?")

    if st.button("Yes"):
        st.session_state.responses["Owns_House"] = 1
        next_step()
    if st.button("No"):
        st.session_state.responses["Owns_House"] = 0
        next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 6 : EDUCATION ----------
elif st.session_state.step == 6:
    card("Education Level")

    for k in EDUCATION_MAP.keys():
        if st.button(k):
            st.session_state.responses["Education_Level"] = EDUCATION_MAP[k]
            next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 7 : LAND ----------
elif st.session_state.step == 7:
    card("Owns Land?")

    if st.button("Yes"):
        st.session_state.responses["Owns_Land"] = 1
        next_step()
    if st.button("No"):
        st.session_state.responses["Owns_Land"] = 0
        next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 8 : LAND DISPUTE ----------
elif st.session_state.step == 8:
    card("Any Land Dispute?")

    if st.button("No"):
        st.session_state.responses["Land_Legal_Dispute"] = 0
        next_step()
    if st.button("Yes"):
        st.session_state.responses["Land_Legal_Dispute"] = 1
        next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 9 : SAVINGS ----------
elif st.session_state.step == 9:
    card("Savings (in Lakhs)")

    sav_lakh = st.slider("Savings", 0, 10_000, step=10)
    st.session_state.responses["Saving"] = int(sav_lakh * 100000)

    if st.button("Next ➡"):
        next_step()
    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 10 : FAMILY ----------
elif st.session_state.step == 10:
    card("Family Structure")

    for k in FAMILY_MAP.keys():
        if st.button(k):
            st.session_state.responses["Family_Structure"] = FAMILY_MAP[k]
            next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 11 : VEHICLES ----------
elif st.session_state.step == 11:
    card("Number of Vehicles")

    veh = st.slider("Vehicles", 1, 8)
    st.session_state.responses["Number_of_Vehicles_Owned"] = int(veh)

    if st.button("Next ➡"):
        next_step()
    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 12 : PERSONALITY ----------
elif st.session_state.step == 12:
    card("Personality Type")

    for k in PERSONALITY_MAP.keys():
        if st.button(k):
            st.session_state.responses["Personality_Type"] = PERSONALITY_MAP[k]
            next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 13 : GYM ----------
elif st.session_state.step == 13:
    card("Gym Category")

    for g in ["Passionate", "Optional", "Obese"]:
        if st.button(g):
            st.session_state.responses["Gym_Category"] = g
            next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 14 : BACKGROUND ----------
elif st.session_state.step == 14:
    card("Background")

    if st.button("Urban"):
        st.session_state.responses["Rural_or_Urban_Background"] = BACKGROUND_MAP["Urban"]
        next_step()
    if st.button("Rural"):
        st.session_state.responses["Rural_or_Urban_Background"] = BACKGROUND_MAP["Rural"]
        next_step()

    if st.button("⬅ Back"):
        prev_step()
    progress_ui()

# ---------- STEP 15 : PREDICTION ----------
elif st.session_state.step == 15:
    card("Result")

    EXPECTED_COLS = [
        "Occupation",
        "Family_Structure",
        "Gym_Category",
        "Personality_Type",
        "Rural_or_Urban_Background",
        "Education_Level",
        "Owns_House",
        "Political_view",
        "Number_of_Vehicles_Owned",
        "Owns_Land",
        "Land_Legal_Dispute",
        "Age",
        "Yearly_Inhand_Income_INR",
        "Saving"
    ]

    row = {c: st.session_state.responses[c] for c in EXPECTED_COLS}
    df = pd.DataFrame([row])

    pred = model.predict(df)[0]

    st.success(f"Dahej Expectation Bracket: {pred} / 10")
    st.caption("⚠️ Educational simulation highlighting social bias")

    if st.button("🔁 Restart"):
        st.session_state.step = 0
        st.session_state.responses = {}
        st.rerun()

