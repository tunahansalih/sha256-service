from sqlalchemy.orm import Session

from . import models

from .. import schemas

def get_message(db: Session, hash: str):
    return db.query(models.MessageHash).filter(models.MessageHash.hash == hash).first()

def create_message(db: Session, message: schemas.MessageHashCreate):
    db_message = models.MessageHash(message=message.message, hash=message.hash)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
