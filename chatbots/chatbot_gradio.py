import gradio as gr


def always_agree(message, history):
    return "Agreed"


if __name__ == "__main__":
    gr.ChatInterface(
        always_agree, title="Your Smart AI Assistant"
    ).launch()
