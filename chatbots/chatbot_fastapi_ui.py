from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class Message(BaseModel):
    message: str


class ChatHistory(BaseModel):
    role: str
    content: str


chat_history = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


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

    # Open index.html in your browser