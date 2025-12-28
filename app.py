import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="AI Learning Path Generator", layout="centered")

st.title("🎓 AI-Powered Personalized Learning Path Generator")
st.markdown("Fill in student details to get a personalized learning path.")

# -----------------------------
# Learning Paths
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
# Input Fields
# -----------------------------
learning_style = st.selectbox(
    "Learning Style",
    ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"]
)

preferred_content = st.selectbox(
    "Preferred Content Type",
    ["Videos", "Articles", "Quizzes", "Projects"]
)

progress = st.slider("Progress (%)", 0, 100, 35)
completed_courses = st.number_input(
    "Completed Courses", min_value=0, max_value=20, value=2
)
average_score = st.slider("Average Score", 0, 100, 44)
session_time = st.slider("Daily Study Time (minutes)", 0, 180, 45)

# -----------------------------
# Rule-Based + ML-Explainable Logic
# -----------------------------
def assign_cluster(progress, avg_score, courses, session_time):
    if avg_score < 50 or progress < 40:
        return 1  # Beginner
    elif avg_score >= 50 and progress < 75:
        return 0  # Intermediate
    else:
        return 2  # Advanced

# -----------------------------
# Generate Learning Path
# -----------------------------
if st.button("Generate Learning Path"):

    cluster = assign_cluster(
        progress,
        average_score,
        completed_courses,
        session_time
    )

    st.success(f"Student Cluster: {cluster}")

    cluster_names = {
        0: "Intermediate Learner",
        1: "Beginner Learner",
        2: "Advanced Learner"
    }

    st.info(f"Category: {cluster_names[cluster]}")

    st.subheader("📚 Recommended Learning Path")

    for step in learning_paths[cluster]:
        st.write("•", step)
