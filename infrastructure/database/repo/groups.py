from typing import Optional

from sqlalchemy import select, update, delete, Sequence, func, cast
from sqlalchemy.dialects.postgresql import insert, JSONB
from sqlalchemy.orm import joinedload

from infrastructure.database.models import Group
from infrastructure.database.repo.base import BaseRepo


class GroupRepo(BaseRepo):
    async def get_or_create_group(
            self,
            chat_id: int,
            user_id: int,
            # и так далее.
    ) -> Group:
        insert_stmt = (
            insert(Group)
            .values(
                chat_id=chat_id,
                user_id=user_id,
                # и так далее.
            )
            .on_conflict_do_update(
                index_elements=[Group.chat_id],
                set_=dict(
                    chat_name=chat_name,
                    # и так далее.
                ),
            )
            .returning(Group)
        )

        result = await self.session.execute(insert_stmt)
        group = result.scalar()
        await self.session.commit()
        return group

    async def update_group(self, chat_id: int, **kwargs):
        pass

    async def get_user_groups(self, user_id: int) -> Sequence["Group"]:
        pass