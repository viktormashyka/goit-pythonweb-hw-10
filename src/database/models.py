from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    description = Column(String, nullable=True)

    def __repr__(self):
        return f"<Contact(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, phone={self.phone}, date_of_birth={self.date_of_birth}, description={self.description})>"
