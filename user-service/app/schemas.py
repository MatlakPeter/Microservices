from uuid import UUID
from pydantic import BaseModel, ConfigDict

class UserCreateDTO(BaseModel):
    id: UUID | None = None
    username: str
    name: str
    role: str = "CLIENT"

class UserDTO(BaseModel):
    id: UUID
    username: str
    name: str
    role: str

    model_config = ConfigDict(from_attributes=True)
