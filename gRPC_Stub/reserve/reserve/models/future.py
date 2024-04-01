from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Future(Base):
    __tablename__ = 'future'
    user_id: str = Column(String, primary_key=True)
    title: str = Column(String)
    content: str = Column(String)
    datetime: datetime = Column(DateTime, default=datetime.utcnow)
