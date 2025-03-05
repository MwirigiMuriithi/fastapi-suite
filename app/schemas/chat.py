# from pydantic import BaseModel
# from typing import List

# class ChatMessageBase(BaseModel):
#     message: str

# class ChatMessageIn(ChatMessageBase):
#     receiver_id: int

# class ChatMessageOut(ChatMessageBase):
#     sender_id: int
#     receiver_id: int
#     timestamp: int

#     class Config:
#         orm_mode = True

from pydantic import BaseModel
from typing import List

class ChatMessageBase(BaseModel):
    message: str

class ChatMessageIn(ChatMessageBase):
    sender_id: int 
    receiver_id: int

class ChatMessageOut(ChatMessageBase):
    sender_id: int
    receiver_id: int
    timestamp: int

    class Config:
        from_attributes = True 
