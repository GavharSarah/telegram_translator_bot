from sqlalchemy import select
from .models import User
from .db_setup import SessionLocal

async def add_user(telegram_id, full_name, phone, language):
    async with SessionLocal() as session:
        user = User(
            telegram_id=telegram_id,
            full_name=full_name,
            phone=phone,
            language=language
        )
        session.add(user)
        await session.commit()

async def get_user(telegram_id):
    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()
