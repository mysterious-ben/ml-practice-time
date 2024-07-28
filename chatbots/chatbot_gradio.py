import gradio as gr


# import os
# from dotenv import load_dotenv
# load_dotenv(verbose=True, override=True)
# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# assert OPENAI_API_KEY


def always_agree(message: str, history: list) -> str:
    return "Agreed???"


with gr.Blocks() as demo:
    gr.ChatInterface(
        always_agree,
        chatbot=gr.Chatbot(show_label=False),
        title="Your Smart AI Assistant",
        examples=["What a lovely day!", "I think I'm very handsome.", "Should I grab some coffee?"],
    )


# To run: gradio chatbots/chatbot_gradio.py
# Docs & examples: https://www.gradio.app/guides/creating-a-chatbot-fast
if __name__ == "__main__":
    demo.launch()
