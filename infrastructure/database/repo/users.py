from datetime import datetime
from typing import Optional, Sequence
from zoneinfo import ZoneInfo

from sqlalchemy import update, select, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import joinedload

from infrastructure.database.models import User, Reminder
from infrastructure.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def get_or_create_user(
            self,
            user_id: int,
            full_name: str,
            language: str,
            username: Optional[str] = None,
            language_code: Optional[str] = None,
    ):
        """
        Создает или обновляет нового пользователя в бд и возвращает объект user.
        """
        insert_stmt = (
            insert(User)
            .values(
                user_id=user_id,
                full_name=full_name,
                # и так далее.
            )
            .on_conflict_do_update(
                index_elements=[User.user_id],
                set_=dict(
                    username=username,
                    full_name=full_name,
                    # и так далее.
                ),
            )
            .returning(User)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one()

    async def update_language(self, user_id: int, language: str) -> Optional[User]:
        pass

    async def update_utc(self, user_id: int, utc: str, city: str) -> Optional[User]:
        pass

    async def get_user_reminders(self, user_id: int) -> Sequence[Reminder]:
        """
        Возвращает список напоминаний для юзера.
        """
        pass

    async def delete_all_user_reminders(self, user_id: int) -> None:
        pass

    async def user_update(self, user_id: int, **kwargs) -> Optional[User]:
        pass

    async def increment_spam(self, user_id: int) -> None:
        pass

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Возвращает объект пользователя по ID.
        Если пользователь не найден, возвращает None.
        """
        pass