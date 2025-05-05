from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

from babel.dates import format_datetime
from sqlalchemy import Integer, DateTime, ForeignKey, String, BIGINT, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Boolean, true
from infrastructure.database.models import Base, Group
from infrastructure.database.models.base import TimestampMixin, TableNameMixin
from tgbot.middlewares.i18n.i18n_format import localization_format_new
from tgbot.misc.locations import get_localized_date


class Group_Reminder(Base, TimestampMixin, TableNameMixin):
    """
    Таблица для хранения напоминаний пользователей в группах.
    """
    reminder_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BIGINT, nullable=False)
    chat_id: Mapped[int] = mapped_column(ForeignKey("groups.chat_id"), nullable=False)
    # и так далее

    group: Mapped["Group"] = relationship("Group", back_populates="group_reminders")

    def to_dict(self):
        return {
            "id": self.reminder_id,
            'chat_id': self.chat_id
            # и так далее

        }

    def __repr__(self):
        return f"<Group_Reminder {self.title} at {self.reminder_time}>"


Group.group_reminders = relationship("Group_Reminder", back_populates="group", cascade="all, delete-orphan")
