import streamlit as st

from chatbot import generate_response

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="📘",
    layout="wide"
)

# ---------------- SESSION STATE ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- TITLE ---------------- #

st.title("📘 AI Personalized Learning Assistant")




# ---------------- SIDEBAR ---------------- #

st.sidebar.header("📚 Student Profile")

# -------- INITIAL SUBJECT LIST -------- #

if "subjects" not in st.session_state:

    st.session_state.subjects = [
        "Operating System",
        "DBMS",
        "Python"
    ]

# -------- ADD NEW SUBJECT -------- #

new_subject = st.sidebar.text_input(
    "Add New Subject"
)

if st.sidebar.button("Add Subject"):

    if (
        new_subject
        and new_subject not in st.session_state.subjects
    ):

        st.session_state.subjects.append(
            new_subject
        )

# -------- SUBJECT SELECTION -------- #

subject = st.sidebar.selectbox(
    "Choose Subject",
    st.session_state.subjects
)

# -------- WEAK TOPICS INPUT -------- #

weak_topics = st.sidebar.text_area(
    "Weak Topics",
    placeholder="Example: Deadlock, Recursion"
)

# -------- WEAK SUBJECTS DISPLAY -------- #

st.sidebar.subheader("⚠ Weak Subjects")

weak_subject_list = [
    topic.strip().lower()
    for topic in weak_topics.split(",")
    if topic.strip()
]

for sub in st.session_state.subjects:

    if sub.lower() in weak_subject_list:

        st.sidebar.markdown(
            f"""
            <div style="
                padding:8px;
                border-radius:10px;
                background-color:#ff4b4b;
                color:white;
                margin-bottom:5px;
                font-weight:bold;
            ">
                ⚠ {sub}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.sidebar.markdown(
            f"""
            <div style="
                padding:8px;
                border-radius:10px;
                background-color:#262730;
                color:white;
                margin-bottom:5px;
            ">
                ✅ {sub}
            </div>
            """,
            unsafe_allow_html=True
        )
# ---------------- DISPLAY CHAT HISTORY ---------------- #

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- CHAT INPUT ---------------- #

user_input = st.chat_input(
    "Ask your question..."
)

# ---------------- HANDLE USER INPUT ---------------- #

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response
    with st.spinner("Thinking..."):

        ai_response = generate_response(
            user_input,
            subject,
            weak_topics
        )

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.write(ai_response)

