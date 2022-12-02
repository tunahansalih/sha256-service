from hashlib import sha256

from fastapi import Depends, FastAPI, HTTPException, Path
from sqlalchemy.orm import Session

from . import schemas
from .db import crud, models
from .db.database import LocalSession, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/messages")
async def messages(message: schemas.MessageHashBase, db: Session = Depends(get_db)):
    hash = sha256(message.message.encode()).hexdigest()
    crud.create_message(db, schemas.MessageHashCreate(
        message=message.message, hash=hash))
    return {"hash": hash}


@app.get("/messages/{hash}")
async def messages(hash: str = Path(max_length=64, min_length=64), db: Session = Depends(get_db)):
    message = crud.get_message(db, hash)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": message.message}
