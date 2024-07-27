from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    message: str


class ChatHistory(BaseModel):
    role: str
    content: str


chat_history = []


@app.post("/chat/")
def chat(message: Message):
    user_message = {"role": "user", "content": message.message}
    chat_history.append(user_message)

    response = "Agreed"
    assistant_message = {"role": "assistant", "content": response}
    chat_history.append(assistant_message)

    return {"response": response, "history": chat_history}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

    # curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"message": "Hello!"}'
