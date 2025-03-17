from datetime import date
from typing import  Optional
from pydantic import BaseModel, Field, ConfigDict


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=50)
    phone: str = Field(max_length=13)
    date_of_birth: date
    description: Optional[str] = Field(None, max_length=150)


class ContactResponse(ContactModel):
    id: int

    model_config = ConfigDict(from_attributes=True)

class ContactUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=50)
    phone: Optional[str] = Field(None, max_length=13)
    date_of_birth: Optional[date] = Field(None)
    description: Optional[str] = Field(None, max_length=150)

class ContactRemove(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
