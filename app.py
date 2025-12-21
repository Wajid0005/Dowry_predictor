import streamlit as st
import pandas as pd
import joblib

# ================= CONFIG =================
st.set_page_config(
    page_title="Dahej Predictor",
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

TOTAL_STEPS = 16

# ================= HELPERS =================
def progress_ui():
    st.progress(st.session_state.step / TOTAL_STEPS)
    st.caption(f"Step {st.session_state.step} / {TOTAL_STEPS}")

def next_step():
    st.session_state.step += 1
    st.rerun()

def prev_step():
    st.session_state.step = max(0, st.session_state.step - 1)
    st.rerun()

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

# ================= SIDEBAR =================
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "",
    ["Main Predictor", "Data", "Actions", "About"]
)

# ================= MAIN PREDICTOR =================
if page == "Main Predictor":

    # ---------- STEP 0 ----------
    if st.session_state.step == 0:
        card("Welcome to Dahej Predictor")

        st.session_state.responses["name"] = st.text_input("Your Name")
        st.session_state.responses["email"] = st.text_input("Email (optional)")

        col1, col2 = st.columns(2)

        if col1.button("♂ Male", key="male"):
            st.session_state.responses["gender"] = "Male"
            next_step()

        if col2.button("♀ Female", key="female"):
            st.session_state.responses["gender"] = "Female"
            st.session_state.step = 99
            st.rerun()

        progress_ui()

    # ---------- FEMALE STOP ----------
    elif st.session_state.step == 99:
        card("Message")

        st.info(
            "This project highlights social bias.\n\n"
            "Dahej is a harmful practice."
        )

        if st.button("Exit"):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.rerun()

    # ---------- STEP 1 : OCCUPATION ----------
    elif st.session_state.step == 1:
        card("Choose your occupation")

        options = [
            "Private Job", "Government Job",
            "Business", "Freelancer",
            "Self-employed", "Unemployed"
        ]

        for opt in options:
            if st.button(opt, key=f"occ_{opt}"):
                st.session_state.responses["Occupation"] = opt
                next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 2 : INCOME ----------
    elif st.session_state.step == 2:
        card("Yearly In-Hand Income (INR)")

        income = st.slider("Income", 0, 10_00_00_000, step=50_000)
        st.session_state.responses["Yearly_Inhand_Income_INR"] = income

        if st.button("Next ➡"):
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 3 : AGE ----------
    elif st.session_state.step == 3:
        card("Your Age")

        age = st.number_input("Age", min_value=18, max_value=45)
        st.session_state.responses["Age"] = age

        if st.button("Next ➡"):
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 4 : POLITICAL VIEW ----------
    elif st.session_state.step == 4:
        card("Political Vibe 😄")

        col1, col2 = st.columns(2)

        if col1.button("Modi", key="modi"):
            st.session_state.responses["Political_view"] = 1
            next_step()

        if col2.button("Rahul", key="rahul"):
            st.session_state.responses["Political_view"] = 0
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

        levels = [
            "No Formal Education", "10th Pass",
            "12th Pass", "Graduate", "Postgraduate+"
        ]

        for lvl in levels:
            if st.button(lvl, key=f"edu_{lvl}"):
                st.session_state.responses["Education_Level"] = lvl
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
        card("Any land dispute?")

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
        st.session_state.responses["Saving"] = sav

        if st.button("Next ➡"):
            next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 10 : FAMILY ----------
    elif st.session_state.step == 10:
        card("Family Structure")

        for f in ["Joint", "Nuclear", "Living Alone"]:
            if st.button(f, key=f"fam_{f}"):
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

        for g in ["Passionate", "Optional", "Obese"]:
            if st.button(g, key=f"gym_{g}"):
                st.session_state.responses["Gym_Category"] = g
                next_step()

        if st.button("⬅ Back"):
            prev_step()

        progress_ui()

    # ---------- STEP 14 : BACKGROUND ----------
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

        EXPECTED_COLS = [
            "Occupation", "Family_Structure", "Gym_Category",
            "Personality_Type", "Rural_or_Urban_Background",
            "Education_Level", "Owns_House", "Political_view",
            "Number_of_Vehicles_Owned", "Owns_Land",
            "Land_Legal_Dispute", "Age",
            "Yearly_Inhand_Income_INR", "Saving"
        ]

        row = {c: st.session_state.responses.get(c, 0) for c in EXPECTED_COLS}
        df = pd.DataFrame([row])

        pred = model.predict(df)[0]

        st.success(f"Predicted Dahej Category: {pred} / 10")

        col1, col2 = st.columns(2)
        if col1.button("🔁 Restart"):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.rerun()

        if col2.button("🔗 Share"):
            st.info("Sharing coming soon")

# ================= OTHER PAGES =================
elif page == "Data":
    st.title("Data")
    st.info("Dataset exploration coming soon.")

elif page == "Actions":
    st.title("Actions")
    st.code("Model training & cleaning shown here.", language="python")

elif page == "About":
    st.title("About")
    st.write("Educational project exploring bias with humor.")
