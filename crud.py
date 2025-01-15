from sqlalchemy.orm import Session
from models import ShortURL
import string, random

def generate_short_id(length: int = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def create_short_url(db: Session, full_url: str):
    short_id = generate_short_id()
    while db.query(ShortURL).filter(ShortURL.short_id == short_id).first():
        short_id = generate_short_id()
    short_url = ShortURL(short_id=short_id, full_url=full_url)
    db.add(short_url)
    db.commit()
    db.refresh(short_url)
    return short_url

def get_short_url(db: Session, short_id: str):
    return db.query(ShortURL).filter(ShortURL.short_id == short_id).first()

def get_stats(db: Session, short_id: str):
    return db.query(ShortURL).filter(ShortURL.short_id == short_id).first()
