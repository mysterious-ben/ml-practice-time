import gradio as gr


def sell_game(message: str, history: list) -> str:
    """This bot will help to sell my majestic horror TTRPG game system."""

    message = message.lower().strip()
    if history:
        last_message = history[-1][1].lower().strip()
    else:
        last_message = ""

    if "yes" in message:
        if "gameplay mechanics" in last_message:
            return (
                "'Peaceful Day in Elysium' features mechanics that simulate the descent into madness. "
                "Players make choices that impact their mental state and uncover dark secrets. "
                "We also have unique systems for different character archetypes. Would you like to know about those?"
            )
        if "story elements" in last_message:
            return (
                "The storyline is set in Elysium, a world that appears peaceful but hides dark secrets. "
                "As players explore, they unravel mysteries that challenge their sanity. "
                "Some of these mysteries involve ancient artifacts and eldritch beings. Interested in more details?"
            )
        if "rules or how the mechanics work" in last_message:
            return (
                "The game uses a unique system focusing on narrative and psychological tension. "
                "Players' actions affect their character's mental state, influencing the story. "
                "We also have a sanity meter that impacts gameplay. Would you like to hear about that?"
            )
        if "character creation" in last_message:
            return (
                "Character creation in 'Peaceful Day in Elysium' is deeply tied to the story. "
                "Players create characters with unique backgrounds that interact with the world's mysteries. "
                "Different backgrounds can lead to unique interactions and story paths. Would you like examples?"
            )
        if "specific story elements" in last_message:
            return (
                "Specific story elements include encounters with mysterious entities, uncovering forbidden knowledge, and dealing with the consequences of one's actions. "
                "These can lead to different endings. Would you like to know about potential endings or more examples?"
            )

    if "no" in message:
        return "Okay, let me know if there's anything else you're curious about!"

    if any(word in message for word in ["what", "info", "information", "about"]):
        return (
            "'Peaceful Day in Elysium' is a horror TTRPG focusing on a slow descent into madness. "
            "Players explore a world filled with eerie calm and unsettling secrets. "
            "Would you like to know more about the gameplay mechanics or the story elements?"
        )
    elif any(word in message for word in ["buy", "purchase", "price"]):
        return (
            "You can purchase 'Peaceful Day in Elysium' from our official store. "
            "It's available in both digital and physical formats. "
            "Would you like a link to the store or more details on the editions?"
        )
    elif any(word in message for word in ["rules", "gameplay", "mechanics"]):
        return (
            "The game uses a unique system to simulate the creeping sense of unease and madness. "
            "Would you like to know more about the rules or how the mechanics work?"
        )
    elif any(word in message for word in ["setting", "world", "story"]):
        return (
            "The story is set in the seemingly tranquil world of Elysium, hiding dark secrets. "
            "As players explore, they encounter unsettling events that slowly unravel the peace. "
            "Are you interested in character creation or exploring the game's lore?"
        )
    else:
        return "I'm here to help you learn more about 'Peaceful Day in Elysium'. What would you like to know?"


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
