from uuid import UUID
from pydantic import BaseModel

class LoginDTO(BaseModel):
    username: str
    password: str

class RegisterDTO(BaseModel):
    username: str
    password: str
    role: str = "CLIENT"

class TokenDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: UUID
    role: str
    