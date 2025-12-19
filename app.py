import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Dahej Predictor",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------- LOAD MODEL --------------------
model = joblib.load("model.pkl")

# -------------------- SESSION STATE --------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "responses" not in st.session_state:
    st.session_state.responses = {}

# -------------------- HELPERS --------------------
TOTAL_STEPS = 16

def progress_ui():
    st.progress(st.session_state.step / TOTAL_STEPS)
    st.caption(f"Step {st.session_state.step} / {TOTAL_STEPS}")

def next_step():
    st.session_state.step += 1
    time.sleep(0.3)
    st.rerun()

def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1
        st.rerun()

def card(title):
    st.markdown(
        f"""
        <div style="
            background:#ffffff;
            padding:30px;
            border-radius:12px;
            box-shadow:0 8px 24px rgba(0,0,0,0.1);
            margin-top:30px;
        ">
        <h3>{title}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- SIDEBAR NAV --------------------
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "",
    ["Main Predictor", "Data", "Actions", "About"]
)

# ==================== MAIN PREDICTOR ====================
if page == "Main Predictor":

    # ---------- STEP 0 : WELCOME ----------
    if st.session_state.step == 0:
        card("Welcome to Dahej Predictor")

        st.session_state.responses["name"] = st.text_input("Your Name")
        st.session_state.responses["email"] = st.text_input("Email (optional)")

        col1, col2 = st.columns(2)
        if col1.button("♂ Male"):
            st.session_state.responses["gender"] = "Male"
            next_step()

        if col2.button("♀ Female"):
            st.session_state.responses["gender"] = "Female"
            st.session_state.step = 99
            st.rerun()

        progress_ui()

    # ---------- FEMALE STOP ----------
    elif st.session_state.step == 99:
        card("Message")

        st.markdown("### 🎥 [ Video Placeholder ]")
        st.info(
            "This project does not apply here.\n\n"
            "Dahej is a social problem rooted in patriarchy."
        )

        if st.button("Exit"):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.rerun()

    # ---------- STEP 1 : OCCUPATION ----------
    elif st.session_state.step == 1:
        card(f"Okay {st.session_state.responses.get('name','')}, choose your occupation")

        opts = [
            "Private Job", "Government Job", "Business",
            "Freelancer", "Self-employed", "Unemployed"
        ]

        for opt in opts:
            if st.button(opt):
                st.session_state.responses["Occupation"] = opt
                next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 2 : INCOME ----------
    elif st.session_state.step == 2:
        card("Select your yearly income (INR)")

        income = st.slider(
            "Income",
            0, 10_00_00_000, step=50_000
        )
        st.session_state.responses["Yearly_Inhand_Income_INR"] = income

        if st.button("Next ➡"):
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 3 : AGE ----------
    elif st.session_state.step == 3:
        card("Enter your age")

        age = st.number_input(
            "Age", min_value=18, max_value=45
        )
        st.session_state.responses["Age"] = age

        if st.button("Next ➡"):
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 4 : POLITICAL ----------
    elif st.session_state.step == 4:
        card("National Stress Preference 😄")

        col1, col2 = st.columns(2)
        if col1.button("Modi"):
            st.session_state.responses["Is_Pookie"] = 1
            next_step()

        if col2.button("Rahul"):
            st.session_state.responses["Is_Pookie"] = 0
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 5 : HOUSE ----------
    elif st.session_state.step == 5:
        card("Do you own a house?")

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

        edu = [
            "No Formal Education", "10th Pass", "12th Pass",
            "Graduate", "Postgraduate+"
        ]

        for e in edu:
            if st.button(e):
                st.session_state.responses["Education_Level"] = e
                next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 7 : LAND ----------
    elif st.session_state.step == 7:
        card("Do you own land?")

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
        card("Any legal dispute on land?")

        if st.button("No Dispute"):
            st.session_state.responses["Land_Legal_Dispute"] = 0
            next_step()
        if st.button("Chacha–Mama Case 😬"):
            st.session_state.responses["Land_Legal_Dispute"] = 1
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 9 : SAVINGS ----------
    elif st.session_state.step == 9:
        card("Savings (in Lakhs)")

        sav = st.slider("Savings", 0, 10_000, step=10)
        st.session_state.responses["Savings_in_Lakhs"] = sav

        if st.button("Next ➡"):
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 10 : FAMILY ----------
    elif st.session_state.step == 10:
        card("Family Structure")

        fam = ["Joint", "Nuclear", "Living Alone"]
        for f in fam:
            if st.button(f):
                st.session_state.responses["Family_Structure"] = f
                next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 11 : VEHICLES ----------
    elif st.session_state.step == 11:
        card("Number of Vehicles")

        veh = st.slider("Vehicles", 0, 7)
        st.session_state.responses["Number_of_Vehicles_Owned"] = veh

        if st.button("Next ➡"):
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 12 : PERSONALITY ----------
    elif st.session_state.step == 12:
        card("Personality Type")

        if st.button("Chill"):
            st.session_state.responses["Personality_Type"] = "Chill"
            next_step()
        if st.button("Ambi"):
            st.session_state.responses["Personality_Type"] = "Ambi"
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 13 : GYM ----------
    elif st.session_state.step == 13:
        card("Gym Category")

        gym = ["Passionate", "Optional", "Obese"]
        for g in gym:
            if st.button(g):
                st.session_state.responses["Gym_Category"] = g
                next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 14 : RURAL / URBAN ----------
    elif st.session_state.step == 14:
        card("Background")

        if st.button("Gao ka chhora"):
            st.session_state.responses["Rural_or_Urban_Background"] = "Rural"
            next_step()
        if st.button("Sheher ka launda"):
            st.session_state.responses["Rural_or_Urban_Background"] = "Urban"
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 15 : PREDICTION ----------
    elif st.session_state.step == 15:
        card("Prediction")

        st.markdown("### 🎥 [ Prediction Video Placeholder ]")

        df = pd.DataFrame([{
            **st.session_state.responses,
            "Owns_House": st.session_state.responses.get("Owns_House",0),
            "Owns_Land": st.session_state.responses.get("Owns_Land",0)
        }])

        pred = model.predict(df)[0]

        st.success(f"Predicted Dahej Category: {pred} / 10")

        col1, col2 = st.columns(2)
        if col1.button("🔁 Restart"):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.rerun()

        if col2.button("🔗 Share"):
            st.info("Sharing feature placeholder")

# ==================== DATA PAGE ====================
elif page == "Data":
    st.title("Data Overview")

    st.subheader("Raw Data Sample")
    st.dataframe(pd.read_csv("data/raw_sample.csv").head(10))

    st.subheader("Cleaned Data Sample")
    st.dataframe(pd.read_csv("data/clean_sample.csv").head(10))

# ==================== ACTIONS PAGE ====================
elif page == "Actions":
    st.title("Actions Performed")

    st.code(
        """
        # Example
        df.dropna()
        df['Income'] = df['Income'].clip(0, 1e7)
        model = RandomForestClassifier()
        """,
        language="python"
    )

    st.markdown("[Open Colab Notebook](https://colab.research.google.com/)")

# ==================== ABOUT PAGE ====================
elif page == "About":
    st.title("About Me")

    st.markdown("### 🎥 [ About Video Placeholder ]")
    st.write(
        "This project explores how social biases "
        "can be modeled and questioned using data."
    )
