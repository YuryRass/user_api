from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.users.model import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User
