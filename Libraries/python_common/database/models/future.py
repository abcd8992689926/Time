from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Future(Base):
    __tablename__ = 'future'
    ID: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: str = Column(String)
    title: str = Column(String)
    content: str = Column(String)
    datetime: datetime = Column(DateTime, default=datetime.now(timezone.utc))

    def __init__(self, user_id: str, title: str, content: str, Datetime: datetime):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.datetime = Datetime

    def as_dict(self):
        excluded_keys = ['ID']
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in excluded_keys}
