from sqlalchemy import Column, Integer, String
from database import Base

class CatApi(Base):
    __tablename__ = 'cat_api'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    breed = Column(String, unique=True, nullable=False, index=True)
    origin = Column(String, nullable=False)
    coat = Column(String, nullable=False)
    body = Column(String, nullable=False)
    pattern = Column(String, nullable=False)


