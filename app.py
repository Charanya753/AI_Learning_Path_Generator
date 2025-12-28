import streamlit as st

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
# Ordered Cluster Logic
# -----------------------------
def assign_cluster(progress, avg_score, courses, session_time):
    # Cluster 0 → Beginner
    if avg_score < 50 or progress < 40:
        return 0

    # Cluster 1 → Intermediate
    elif avg_score < 75 or progress < 75:
        return 1

    # Cluster 2 → Advanced
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
