from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Repository:
    def __init__(self, db_url: str):
        engine = create_engine(db_url)
        self.Session = sessionmaker(bind=engine)

    def add(self, obj):
        with self.Session() as session:
            session.add(obj)
            session.commit()
