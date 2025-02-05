from app.models.chat import Chat
from app.schemas.chat import ChatMessageIn
from sqlalchemy.orm import Session

def create_chat_message(db: Session, chat: ChatMessageIn):
    db_chat = Chat(sender_id=chat.sender_id, receiver_id=chat.receiver_id, message=chat.message, timestamp=chat.timestamp)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat