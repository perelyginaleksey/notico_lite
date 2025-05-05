from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, false, JSON, Integer
from sqlalchemy import text, BIGINT, Boolean, true
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class User(Base, TimestampMixin, TableNameMixin):
    """
    Таблица для хранения данных о пользователе.
    """
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    full_name: Mapped[str] = mapped_column(String(128))
    # и так далее

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "full_name": self.full_name
                # и так далее
        }

    def __repr__(self):
        return f"<User {self.user_id} {self.username} {self.full_name}>"
