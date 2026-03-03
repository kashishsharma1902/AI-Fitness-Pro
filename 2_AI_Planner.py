import streamlit as st
import google.generativeai as genai

st.title("🥗 AI Personalized Planner (Gemini AI)")

# ✅ FIRST: Check if user_data exists

if "user_data" not in st.session_state:
    st.error("Please fill details on Home page first.")
    st.stop()

user_data = st.session_state["user_data"]

st.write("User Info:")
st.write(user_data)

# ✅ Google API key directly
api_key = "AIzaSyCsrJ7IFntlC0FNjqBPdxY135hKSie8uLQ"

if not api_key:
    st.error("Google API key not configured")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

data = st.session_state["user_data"]

if st.button("Generate My Custom Plan"):

    prompt = f"""
    Create a detailed structured fitness plan.

    User Profile:
    Gender: {data['gender']}
    Weight: {data['weight']} kg
    Age: {data['age']}
    Goal: {data['goal']}
    Daily Calories Target: {data['tdee']} kcal

    Include:
    1. Full day meal plan (Breakfast, Lunch, Dinner, Snacks)
    2. Weekly workout routine (sets and reps)
    3. Recovery and hydration advice
    4. Protein recommendation
    """

    with st.spinner("Generating your plan..."):

        try:
            response = model.generate_content(prompt)
            st.markdown("## 📋 Your Personalized Plan")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error generating plan: {e}")