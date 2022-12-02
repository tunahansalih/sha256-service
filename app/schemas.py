from pydantic import BaseModel

class MessageHashBase(BaseModel):
    message: str

class MessageHashCreate(MessageHashBase):
    hash: str

class MessageHash(MessageHashBase):
    id: int
    hash: str

    class Config:
        orm_mode = True

    