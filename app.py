import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load saved models
# -----------------------------
@st.cache_resource
def load_models():
    kmeans = joblib.load("kmeans_model.pkl")
    scaler = joblib.load("scaler.pkl")
    le_style = joblib.load("learningstyle_encoder.pkl")
    le_content = joblib.load("content_encoder.pkl")
    return kmeans, scaler, le_style, le_content

kmeans, scaler, le_style, le_content = load_models()

# -----------------------------
# Learning paths per cluster
# -----------------------------
learning_paths = {
    0: [
        "Interactive Video Tutorials",
        "Hands-on Practice",
        "Weekly Assessments",
        "Mini Project"
    ],
    1: [
        "Conceptual Reading Materials",
        "Quizzes",
        "Case Studies",
        "Guided Assignments"
    ],
    2: [
        "Advanced Projects",
        "Real-world Applications",
        "Mock Interviews",
        "Capstone Project"
    ]
}

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="AI Learning Path Generator", layout="centered")
st.title("🎓 AI-Powered Personalized Learning Path Generator")

st.markdown("Fill in student details to get a personalized learning path.")

# Input fields
learning_style = st.selectbox(
    "Learning Style",
    le_style.classes_
)

preferred_content = st.selectbox(
    "Preferred Content Type",
    le_content.classes_
)

progress = st.slider("Progress (%)", 0, 100, 50)
completed_courses = st.number_input(
    "Completed Courses", min_value=0, max_value=20, value=2
)
average_score = st.slider("Average Score", 0, 100, 70)
session_time = st.slider("Daily Study Time (minutes)", 0, 180, 45)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Generate Learning Path"):
    # Create input dataframe
    input_df = pd.DataFrame([{
        "LearningStyle": learning_style,
        "Progress": progress,
        "CompletedCourses": completed_courses,
        "AverageScore": average_score,
        "PreferredContent": preferred_content,
        "SessionTime": session_time
    }])

    # Encode categorical features
    input_df["LearningStyle"] = le_style.transform(input_df["LearningStyle"])
    input_df["PreferredContent"] = le_content.transform(input_df["PreferredContent"])

    # Scale features
    scaled_input = scaler.transform(input_df)

    # Predict cluster
    cluster = kmeans.predict(scaled_input)[0]

    # Display result
    st.success(f"Student Cluster: {cluster}")
    st.subheader("📚 Recommended Learning Path")

    for step in learning_paths[cluster]:
        st.write("•", step)
