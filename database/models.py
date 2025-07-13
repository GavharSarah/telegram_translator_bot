from sqlalchemy import Column, Integer, String, BigInteger
from .db_setup import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    language = Column(String, nullable=True)

