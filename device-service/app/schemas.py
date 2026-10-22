from uuid import UUID
from pydantic import BaseModel, ConfigDict

class DeviceCreateDTO(BaseModel):
    name: str
    address: str | None = None
    max_consumption: float
    user_id: UUID | None = None

class DeviceDTO(BaseModel):
    id: UUID
    name: str
    address: str | None
    max_consumption: float
    user_id: UUID | None

    model_config = ConfigDict(from_attributes=True)
