import gradio as gr


def always_agree(message: str, history: list) -> str:
    return "Agreed"


# To run: python chatbots/chatbot_gradio.py
# Docs & examples: https://www.gradio.app/guides/creating-a-chatbot-fast
if __name__ == "__main__":
    gr.ChatInterface(
        always_agree,
        chatbot=gr.Chatbot(show_label=False),
        title="Your Smart AI Assistant",
        examples=["What a lovely day!", "I think I'm very handsome.", "Should I grab some coffee?"],
    ).launch()
