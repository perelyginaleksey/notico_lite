from datetime import datetime
from typing import Optional

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import joinedload

from infrastructure.database.models import Reminder
from infrastructure.database.repo.base import BaseRepo


class ReminderRepo(BaseRepo):
    async def get_or_create_reminder(
            self,
            user_id: int,
            title: str,
            reminder_time: datetime,
            # и так далее.
    ):
        insert_stmt = (
            insert(Reminder)
            .values(
                user_id=user_id,
                title=title,
                reminder_time=reminder_time,
                # и так далее.
            )
            .on_conflict_do_update(
                index_elements=[Reminder.reminder_id],
                set_=dict(
                    title=title,
                    reminder_time=reminder_time,
                    # и так далее.
                ),
            )
            .returning(Reminder)
        )

        result = await self.session.execute(insert_stmt)
        await self.session.commit()
        reminder_id = result.scalar().reminder_id
        reminder = await self.session.execute(
            select(Reminder).options(joinedload(Reminder.user)).where(Reminder.reminder_id == reminder_id)
        )
        return reminder.scalar()

    async def get_reminder_by_id(self, user_id: int, reminder_id: int) -> Optional[Reminder]:
        pass

    async def update_reminder_status(self, user_id: int, reminder_id: int, status: bool) -> Optional[Reminder]:
        pass

    async def update_reminder_time_and_status(self, user_id: int, reminder_id: int, new_time: datetime, status: bool):
        pass

    async def update_reminder(self, user_id: int, reminder_id: int, **kwargs):
        pass

    async def delete_reminder(self, user_id: int, reminder_id: int) -> bool:
        stmt = (
            delete(Reminder)
            .where(Reminder.user_id == user_id, Reminder.reminder_id == reminder_id)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0
