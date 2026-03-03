import streamlit as st

st.set_page_config(
    page_title="AI Fitness Hub",
    layout="wide",
    page_icon="💪"
)

st.title("💪 AI Fitness Pro")
st.subheader("Your AI-Powered Health & Nutrition Companion")

import streamlit as st



col1, col2 = st.columns(2)



with col1:
    st.markdown("""
    ### What this app does:
    - 📊 Calculates your BMR & TDEE
    - 🥗 Generates AI meal plans
    - 🏋️ Creates workout routines
    - 📈 Helps track progress
    """)

    if st.button("Get Started →"):
        st.success("Use the sidebar to navigate to the Calculator page.")

with col2:
    st.info(
        "💡 **BMR** is the number of calories your body burns at complete rest.\n\n"
        "**TDEE** includes your daily activity."
    )

st.divider()

st.image(
    "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&q=80&w=1000",
    caption="Consistency is Key",
    use_container_width=True
)