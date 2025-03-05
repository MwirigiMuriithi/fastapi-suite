# from sqlalchemy import Column, Integer, String, Text, ForeignKey
# from sqlalchemy.orm import relationship
# from app.db.session import Base

# class Blog(Base):
#     __tablename__ = 'blogs'
    
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(Text)
#     created_at = Column(String)  # You can use DateTime, but for simplicity, we're using a string here.
#     user_id = Column(Integer, ForeignKey('users.id'))
    
#     user = relationship("User", back_populates="blogs")

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.db.session import Base

# class Blog(Base):
#     __tablename__ = "blogs"
    
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     owner_id = Column(Integer, ForeignKey("users.id"))
    
#     owner = relationship("User", back_populates="blogs")


from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base
import datetime

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow) 

    owner = relationship("User", back_populates="blogs")
