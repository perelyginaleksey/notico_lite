from sqlalchemy import Integer, ForeignKey, String, BIGINT, text, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infrastructure.database.models import Base, User
from infrastructure.database.models.base import TimestampMixin, TableNameMixin


class Group(Base, TimestampMixin, TableNameMixin):
    """
    Таблица групп, в которые добавлен бот.
    """
    chat_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    # и так далее

    user: Mapped["User"] = relationship("User", back_populates="groups")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "chat_id": self.chat_id,
            # и так далее
        }

    def __repr__(self):
        return f"<Group {self.chat_name}>"


User.groups = relationship("Group", back_populates="user", cascade="all, delete-orphan")
