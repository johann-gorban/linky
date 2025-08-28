from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

    
class LinkRecord(Base):
    __tablename__= 'links'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    message_id: Mapped[str | None] = mapped_column(String, nullable=False)
    user_id: Mapped[str | None] = mapped_column(String, nullable=False)
    chat_id: Mapped[str | None] = mapped_column(String, nullable=True)
    url: Mapped[str | None] = mapped_column(String, nullable=False)
