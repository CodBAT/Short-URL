from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from crud import create_short_url, get_short_url, get_stats
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Модель запроса
class URLRequest(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(request: URLRequest, db: Session = Depends(get_db)):
    short_url = create_short_url(db, request.url)
    return {"short_url": short_url.short_id}

@app.get("/{short_id}")
def redirect_to_url(short_id: str, db: Session = Depends(get_db)):
    short_url = get_short_url(db, short_id)
    if not short_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(short_url.full_url)

@app.get("/stats/{short_id}")
def get_short_url_stats(short_id: str, db: Session = Depends(get_db)):
    short_url = get_stats(db, short_id)
    if not short_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"short_id": short_url.short_id, "full_url": short_url.full_url}
