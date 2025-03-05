# from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# from app.services.chat import send_message, get_messages
# from app.schemas.chat import ChatMessageIn, ChatMessageOut
# from app.db.session import SessionLocal
# from fastapi.responses import HTMLResponse
# from typing import List

# router = APIRouter()

# clients: List[WebSocket] = []

# @router.websocket("/ws/{user_id}")
# async def websocket_endpoint(websocket: WebSocket, user_id: int):
#     await websocket.accept()
#     clients.append(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             for client in clients:
#                 await client.send_text(f"User {user_id} says: {data}")
#     except WebSocketDisconnect:
#         clients.remove(websocket)

# @router.post("/send_message/", response_model=ChatMessageOut)
# def send_chat_message(chat: ChatMessageIn, db: SessionLocal):
#     return send_message(db=db, chat=chat)

# @router.get("/get_messages/{sender_id}/{receiver_id}", response_model=List[ChatMessageOut])
# def fetch_chat_history(sender_id: int, receiver_id: int, db: SessionLocal):
#     return get_messages(db=db, sender_id=sender_id, receiver_id=receiver_id)


from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from typing import List
from app.services.chat import send_message, get_messages
from app.schemas.chat import ChatMessageIn, ChatMessageOut
from app.db.session import get_db  # Import the dependency
from fastapi.responses import HTMLResponse

router = APIRouter()

clients: List[WebSocket] = []

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in clients:
                await client.send_text(f"User {user_id} says: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)

@router.post("/send_message/", response_model=ChatMessageOut)
def send_chat_message(chat: ChatMessageIn, db: Session = Depends(get_db)):
    return send_message(db=db, chat=chat)

@router.get("/get_messages/{sender_id}/{receiver_id}", response_model=List[ChatMessageOut])
def fetch_chat_history(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    return get_messages(db=db, sender_id=sender_id, receiver_id=receiver_id)
