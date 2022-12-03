from hashlib import sha256

from fastapi import Depends, FastAPI, HTTPException, Path
from . import schemas
from .db import database, crud

def get_dynamo_table():
    table = database.initialize_db()
    return table

app = FastAPI()

@app.post("/messages")
async def messages(message: schemas.MessageHashBase, db = Depends(get_dynamo_table)):
    hash = sha256(message.message.encode()).hexdigest()
    
    if crud.get_message(db, hash) is None:
        crud.create_message(db, schemas.MessageHash(message=message.message, hash=hash))
    return {"hash": hash}


@app.get("/messages/{hash}")
async def messages(hash: str = Path(max_length=64, min_length=64), db = Depends(get_dynamo_table)):
    message = crud.get_message(db, hash)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": message.message}
