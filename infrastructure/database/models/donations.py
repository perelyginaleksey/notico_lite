import datetime
from typing import Optional

from sqlalchemy import Text, Integer, String, BIGINT, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models import Base, User
from infrastructure.database.models.base import TimestampMixin, TableNameMixin


class Donation(Base, TimestampMixin, TableNameMixin):
    """
    Таблица для хранения донатов пользователей тг звездами.
    """
    donation_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    # и так далее

    user: Mapped["User"] = relationship("User", back_populates="donations")

    def to_dict(self):
        return {
            "donation_id": self.donation_id,
            "amount": self.amount,
            # и так далее
        }

    def __repr__(self):
        return f"<Donation {self.amount} by user {self.user.user_id}>"


User.donations = relationship("Donation", back_populates="user", cascade="all, delete-orphan")
