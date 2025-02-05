from datetime import datetime
from app.db import crud
from app.models.chat import Chat
from app.schemas.chat import ChatMessageIn, ChatMessageOut
from app.db.session import SessionLocal

def send_message(db: SessionLocal, chat: ChatMessageIn):
    new_message = Chat(
        sender_id=chat.sender_id,
        receiver_id=chat.receiver_id,
        message=chat.message,
        timestamp=int(datetime.now().timestamp())
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

def get_messages(db: SessionLocal, sender_id: int, receiver_id: int):
    return db.query(Chat).filter(
        (Chat.sender_id == sender_id & Chat.receiver_id == receiver_id) |
        (Chat.sender_id == receiver_id & Chat.receiver_id == sender_id)
    ).all()
