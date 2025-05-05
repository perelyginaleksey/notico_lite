from datetime import datetime
from typing import Optional

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import joinedload

from infrastructure.database.models import Reminder, Donation
from infrastructure.database.repo.base import BaseRepo


class DonationRepo(BaseRepo):
    async def get_or_create_donation(
            self,
            user_id: int,
            amount: int,
            status: str = "pending",
            transaction_id: str = None
    ):
        """
        Создает или обновляет запись Donation. #
        """
        insert_stmt = ()
        # и так далее.

        result = await self.session.execute(insert_stmt)
        await self.session.commit()
        donation_id = result.scalar().donation_id

        donation_query = await self.session.execute('some_code')
        return donation_query.scalar()

    async def update_donation(self, user_id: int, donation_id: int, **kwargs):
        pass

    async def delete_donation(self, user_id: int, donation_id: int):
        pass
