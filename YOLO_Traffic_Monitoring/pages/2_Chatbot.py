import streamlit as st
from chatbot.chatbot import get_answer

st.title("🤖 Traffic Rules Chatbot")

st.write("Ask questions related to traffic rules and road signs.")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = get_answer(question)
        st.success(answer)

st.markdown("---")

st.subheader("Example Questions")

st.write("• What does a red signal mean?")
st.write("• Is helmet compulsory?")
st.write("• What is the speed limit?")
st.write("• What is a zebra crossing?")
st.write("• What does a no parking sign mean?")