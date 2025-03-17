from datetime import date, timedelta
from typing import List, Optional

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdate


class ContactRepository:
    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_contacts(self, skip: int, limit: int) -> List[Contact]:
        stmt = select(Contact).offset(skip).limit(limit)
        contacts = await self.db.execute(stmt)
        return contacts.scalars().all()

    async def get_contact_by_id(self, contact_id: int) -> Contact | None:
        stmt = select(Contact).filter_by(id=contact_id)
        contact = await self.db.execute(stmt)
        return contact.scalar_one_or_none()

    async def create_contact(self, body: ContactModel) -> Contact:
        contact = Contact(**body.dict(exclude_unset=True))
        self.db.add(contact)
        await self.db.commit()
        await self.db.refresh(contact)
        return contact

    async def remove_contact(self, contact_id: int) -> Contact | None:
        contact = await self.get_contact_by_id(contact_id)
        if contact:
            await self.db.delete(contact)
            await self.db.commit()
        return contact

    async def update_contact(
        self, contact_id: int, body: ContactUpdate
    ) -> Contact | None:
        contact = await self.get_contact_by_id(contact_id)
        if contact:
            for key, value in body.dict(exclude_unset=True).items():
                setattr(contact, key, value)
            await self.db.commit()
            await self.db.refresh(contact)
        return contact
    
    async def search_contacts(self, first_name: Optional[str], last_name: Optional[str], email: Optional[str]) -> List[Contact]:
        stmt = select(Contact).filter(
            and_(
                Contact.first_name.ilike(f"%{first_name}%") if first_name else True,
                Contact.last_name.ilike(f"%{last_name}%") if last_name else True,
                Contact.email.ilike(f"%{email}%") if email else True
            )
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_upcoming_birthdays(self) -> List[Contact]:
        today = date.today()
        next_week = today + timedelta(days=7)
        stmt = select(Contact).filter(
            and_(
                Contact.date_of_birth >= today,
                Contact.date_of_birth <= next_week
            )
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()
