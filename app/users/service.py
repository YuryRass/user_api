from collections.abc import AsyncGenerator

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.model import User
from app.users.repository import UserRepository


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepository


async def provide_users_service(
    db_session: AsyncSession,
) -> AsyncGenerator[UserService]:
    async with UserService.new(session=db_session) as service:
        yield service
