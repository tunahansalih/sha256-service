from pydantic import BaseModel

class MessageHashBase(BaseModel):
    message: str

class MessageHash(MessageHashBase):
    hash: str

    