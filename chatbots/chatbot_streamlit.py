import streamlit as st


# import os
# from dotenv import load_dotenv
# load_dotenv(verbose=True, override=True)
# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# assert OPENAI_API_KEY


def always_agree(message: str, history: list) -> str:
    return "Agreed"


# To run: streamlit run chatbots/chatbot_streamlit.py
# Docs and examples: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps
if __name__ == "__main__":
    st.title("Your Smart AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = always_agree(prompt, st.session_state.messages)
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
