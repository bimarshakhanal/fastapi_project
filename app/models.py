'''Collection of data models used in this fastapi app'''
from uuid import UUID, uuid4
from pydantic import BaseModel


class Employee(BaseModel):
    '''Model representig an Employee'''
    id: UUID = uuid4()
    name: str
    department: str
