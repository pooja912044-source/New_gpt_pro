
import streamlit as st
import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="New_gpt_pro", page_icon="🤖")
st.title("💬 New_gpt_pro - Query Bot")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Input box
user_query = st.text_input("Enter your query:")

if user_query:
    # Save user query
    st.session_state["messages"].append({"role": "user", "content": user_query})

    with st.spinner("Thinking..."):
        response = model.generate_content(user_query)
        bot_reply = response.text

    # Save bot reply
    st.session_state["messages"].append({"role": "bot", "content": bot_reply})

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**New_gpt_pro:** {msg['content']}")
