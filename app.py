import streamlit as st
from agents import planner_agent, quiz_agent, motivation_agent

st.set_page_config(page_title="Study Buddy AI Agent")

st.title("📚 Study Buddy AI Agent")
st.write("An AI-powered study assistant for students.")

topic = st.text_input("Enter a topic")

if st.button("Generate"):

    st.subheader("📅 Study Plan Agent")
    st.write(planner_agent(topic))

    st.subheader("📝 Quiz Agent")
    st.write(quiz_agent(topic))

    st.subheader("💡 Motivation Agent")
    st.write(motivation_agent())