from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.repo.donations import DonationRepo
from infrastructure.database.repo.groups import GroupRepo
from infrastructure.database.repo.reminder_group import ReminderGroupRepo
from infrastructure.database.repo.reminders import ReminderRepo
from infrastructure.database.repo.users import UserRepo
from infrastructure.database.setup import create_engine


@dataclass
class RequestsRepo:
    """
    Репозиторий для обработки операций с базами данных. Этот класс содержит все хранилища для моделей баз данных.
    Вы можете добавить дополнительные хранилища в качестве свойств к этому классу, чтобы они были легко доступны.
    """

    session: AsyncSession

    @property
    def users(self) -> UserRepo:
        return UserRepo(self.session)

    @property
    def reminders(self) -> ReminderRepo:
        return ReminderRepo(self.session)


    @property
    def donations(self) -> DonationRepo:
        return DonationRepo(self.session)

    @property
    def groups(self) -> GroupRepo:
        return GroupRepo(self.session)

    @property
    def reminder_group(self) -> ReminderGroupRepo:
        return ReminderGroupRepo(self.session)


if __name__ == "__main__":
    from infrastructure.database.setup import create_session_pool
    from tgbot.config import Config


    async def example_usage(config: Config):
        """
        Example.
        """
        engine = create_engine(config.db)
        session_pool = create_session_pool(engine)

        async with session_pool() as session:
            repo = RequestsRepo(session)

            # Replace user details with the actual values
            user = await repo.users.get_or_create_user(
                user_id=12356,
                full_name="John Doe",
                language="en",
                username="johndoe",
            )
