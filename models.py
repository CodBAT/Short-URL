from sqlalchemy import Column, Integer, String
from database import Base

class ShortURL(Base):
    __tablename__ = "shorturls"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String, unique=True, index=True)
    full_url = Column(String)
