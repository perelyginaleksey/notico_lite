from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

from babel.dates import format_datetime
from sqlalchemy import Integer, DateTime, ForeignKey, String, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Boolean, true
from infrastructure.database.models import Base, User
from infrastructure.database.models.base import TimestampMixin, TableNameMixin
from tgbot.middlewares.i18n.i18n_format import localization_format_new
from tgbot.misc.locations import get_localized_date


class Reminder(Base, TimestampMixin, TableNameMixin):
    """
    Таблица для хранения напоминаний пользователей.
    """
    reminder_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    title: Mapped[str] = mapped_column(String(5000), nullable=False)
    # и так далее

    user: Mapped["User"] = relationship("User", back_populates="reminders")

    def to_dict(self):
        return {
            "id": self.reminder_id,
            "title": self.title,
            # и так далее

        }

    def __repr__(self):
        return f"<Reminder {self.title} at {self.reminder_time}>"


User.reminders = relationship("Reminder", back_populates="user", cascade="all, delete-orphan")
