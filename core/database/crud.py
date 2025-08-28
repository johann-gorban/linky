from .models import LinkRecord, Base
from .config import MAIN_DB_PATH

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import List

import asyncio


class Database:
    def __init__(self):
        self.engine = create_async_engine(f'sqlite+aiosqlite:///{MAIN_DB_PATH}',
                                          echo=False)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def close(self):
        await self.engine.dispose()

    async def init(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_links_by_message_id(self, message_id: str) -> List[str]:
        async with self.SessionLocal() as session:
            db_request = select(LinkRecord).where(LinkRecord.message_id == message_id)
            result = await session.execute(db_request)
            return result.scalars().all()
        
    async def get_links_by_user_id(self, user_id: str) -> List[str]:
        async with self.SessionLocal() as session:
            db_request = select(LinkRecord).where(LinkRecord.user_id == user_id)
            result = await session.execute(db_request)
            return result.scalars().all()
        
    async def get_links_by_chat_id(self, chat_id: str) -> List[str]:
        async with self.SessionLocal() as session:
            db_request = select(LinkRecord).where(LinkRecord.user_id == chat_id)
            result = await session.execute(db_request)
            return result.scalars().all()
        
    async def get_all_links(self) -> List[str]:
        async with self.SessionLocal() as session:
            db_request = select(LinkRecord)
            result = await session.execute(db_request)
            return result.scalars().all()
        
    async def add_link(self, url: str, message_id: str, user_id: str, chat_id: str):
        async with self.SessionLocal() as session:
            link_rec = LinkRecord(
                message_id=message_id,
                user_id=user_id,
                chat_id=chat_id,
                url=url
            )
            session.add(link_rec)


db = Database()

async def init_db():
    await db.init()

asyncio.run(init_db())