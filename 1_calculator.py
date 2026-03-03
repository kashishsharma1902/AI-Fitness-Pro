import streamlit as st

st.title("📊 Personal Metrics Calculator")

with st.form("metrics_form"):
    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        height = st.number_input("Height (cm)", min_value=120, max_value=230, value=170)
        age = st.number_input("Age", min_value=15, max_value=80, value=25)

    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
        activity = st.selectbox(
            "Activity Level",
            ["Sedentary", "Light", "Moderate", "Very Active"]
        )
        goal = st.selectbox(
            "Goal",
            ["Lose Weight", "Maintain", "Build Muscle"]
        )

    submitted = st.form_submit_button("Calculate")

if submitted:

    # Mifflin-St Jeor Formula
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multiplier = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Very Active": 1.725
    }

    tdee = bmr * activity_multiplier[activity]

    # Goal adjustments
    if goal == "Lose Weight":
        target_calories = tdee - 400
    elif goal == "Build Muscle":
        target_calories = tdee + 300
    else:
        target_calories = tdee

    st.session_state["user_data"] = {
        "weight": weight,
        "height": height,
        "age": age,
        "gender": gender,
        "goal": goal,
        "tdee": round(target_calories)
    }

    st.success("✅ Data Saved! Now go to AI Planner.")

    st.metric("🔥 Daily Target Calories", f"{round(target_calories)} kcal")