'''Collection of data models used in this fastapi app'''
from uuid import UUID, uuid4
from pydantic import BaseModel, field_validator


class Employee(BaseModel):
    '''Model representig an Employee'''
    id: UUID = uuid4()
    name: str
    department: str

    @field_validator('name')
    def name_must_not_be_empty(self, value):
        '''Prevent employee object creation with empty name'''
        if not value:
            raise ValueError("Name cannot be empty")
        return value
