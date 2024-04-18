from pydantic import BaseModel, UUID, field_validator, UUID4


class Employee(BaseModel):
    id: UUID = UUID4()
    name: str
    department: str

    @field_validator('name')
    def name_must_not_be_empty(cls, value):
        if not value:
            raise ValueError("Name cannot be empty")
        return value
