import gradio as gr


def always_agree(message: str, history: list) -> str:
    return "Agreed"


# To run: python chatbots/chatbot_gradio.py
# Docs & examples: https://www.gradio.app/guides/creating-a-chatbot-fast
if __name__ == "__main__":
    gr.ChatInterface(always_agree, title="Your Smart AI Assistant").launch()
