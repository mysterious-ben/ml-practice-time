import os

import gradio as gr
import openai
from dotenv import load_dotenv


load_dotenv(verbose=True, override=True)
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
assert OPENAI_API_KEY
client = openai.OpenAI(api_key=OPENAI_API_KEY)


sell_role_prompt = (
    "You are a knowledgeable and friendly chatbot designed to promote and provide information about the horror TTRPG game 'Peaceful Day in Elysium'. "
    "This game immerses players in a world where they experience a slow descent into madness, uncover dark secrets, and explore eerie environments. "
    "Your goal is to engage users in conversation, explain the unique aspects of the game, including gameplay mechanics, story elements, and character creation, and encourage them to purchase the game. "
    "Always respond in an engaging manner, guiding the conversation towards exploring different features of the game. "
    "Reply in one or two sentences to make it more dynamic. "
    "End with a question to keep the conversation going."
)


def sell_game(message: str, history: list):
    history_openai_format = [{"role": "system", "content": sell_role_prompt}]
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=history_openai_format, temperature=0.7, stream=True
    )
    # message = response.choices[0].message.content
    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message


init_message = "<strong>Welcome to 'Peaceful Day in Elysium'!</strong><br>This is a horror TTRPG about a slow descent into madness. Shall we start?"

with gr.Blocks() as demo:
    gr.ChatInterface(
        sell_game,
        chatbot=gr.Chatbot(placeholder=init_message, show_label=False),
        # textbox=gr.Textbox(placeholder="Ask me anything about 'Peaceful Day in Elysium'"),
        title="Peaceful Day in Elysium Chatbot",
        examples=["What is this game about?", "How can I buy it?", "Is there a setting?"],
    )


# To run: gradio chatbots/answers_chatbot_gradio_rules.py
# Docs & examples: https://www.gradio.app/guides/creating-a-chatbot-fast
if __name__ == "__main__":
    demo.launch()
