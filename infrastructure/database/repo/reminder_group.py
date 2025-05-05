from datetime import datetime
from typing import Optional

from sqlalchemy import select, update, delete, Sequence
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import joinedload, selectinload

from infrastructure.database.models import Group, Group_Reminder
from infrastructure.database.repo.base import BaseRepo


class ReminderGroupRepo(BaseRepo):
    async def get_or_create_group_reminder(
            self,
            user_id: int,
            chat_id: int,
            # и так далее.
    ) -> Group_Reminder:
        insert_stmt = (
            insert(Group_Reminder)
            .values(
                user_id=user_id,
                chat_id=chat_id,
                # и так далее.
            )
            .on_conflict_do_update(
                index_elements=[Group_Reminder.reminder_id],
                set_=dict(
                    title=title,
                    reminder_time=reminder_time,
                    # и так далее.
                ),
            )
            .returning(Group_Reminder.reminder_id)
        )

        result = await self.session.execute(insert_stmt)
        reminder_id = result.scalar()
        await self.session.commit()

        group_reminder = await self.session.get(
            Group_Reminder,
            reminder_id,
            options=[selectinload(Group_Reminder.group)]
        )

        return group_reminder

    async def get_group_reminders(self, chat_id: int):
        """
        Возвращает список напоминаний для указанной группы.
        """
        pass

    async def delete_reminder_group(self, reminder_id: int) -> bool:
        pass

    async def delete_all_group_reminders(self, chat_id: int) -> None:
        """
        Удаляет все напоминания группы.
        """
        pass
