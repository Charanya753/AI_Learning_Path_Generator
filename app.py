import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Learning Path Generator",
    layout="centered"
)

st.title("🎓 AI-Powered Personalized Learning Path Generator")
st.markdown("Fill in student details to get a personalized learning path.")

# -----------------------------
# Learning Paths (Ordered)
# -----------------------------
learning_paths = {
    0: [  # Beginner
        "Conceptual Reading Materials",
        "Basic Quizzes",
        "Guided Assignments",
        "Introductory Case Studies"
    ],
    1: [  # Intermediate
        "Interactive Video Tutorials",
        "Hands-on Practice",
        "Weekly Assessments",
        "Mini Projects"
    ],
    2: [  # Advanced
        "Advanced Projects",
        "Real-world Applications",
        "Mock Interviews",
        "Capstone Project"
    ]
}

# -----------------------------
# User Inputs
# -----------------------------
learning_style = st.selectbox(
    "Learning Style",
    ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"]
)

preferred_content = st.selectbox(
    "Preferred Content Type",
    ["Videos", "Articles", "Quizzes", "Projects"]
)

progress = st.slider("Progress (%)", 0, 100, 25)
completed_courses = st.number_input(
    "Completed Courses",
    min_value=0,
    max_value=20,
    value=1
)
average_score = st.slider("Average Score", 0, 100, 40)
session_time = st.slider("Daily Study Time (minutes)", 0, 180, 150)

# -----------------------------
# Cluster Assignment Logic
# -----------------------------
def assign_cluster(progress, avg_score, courses, session_time):
    """
    Cluster Mapping:
    0 → Beginner
    1 → Intermediate
    2 → Advanced
    """

    # Beginner
    if progress <= 40 and avg_score <= 50:
        return 0

    # Intermediate
    elif progress <= 75 and avg_score <= 75:
        return 1

    # Advanced
    else:
        return 2

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

    cluster_names = {
        0: "Beginner Learner",
        1: "Intermediate Learner",
        2: "Advanced Learner"
    }

    st.success(f"Student Cluster: {cluster}")
    st.info(f"Category: {cluster_names[cluster]}")

    st.subheader("📚 Recommended Learning Path")

    for step in learning_paths[cluster]:
        st.write("•", step)
