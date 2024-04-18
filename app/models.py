from pydantic import BaseModel, field_validator
from uuid import UUID, uuid4


class Employee(BaseModel):
    id: UUID = uuid4()
    name: str
    department: str

    @field_validator('name')
    def name_must_not_be_empty(cls, value):
        if not value:
            raise ValueError("Name cannot be empty")
        return value
