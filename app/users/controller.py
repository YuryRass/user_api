from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.params import Parameter

from app.users.schema import SUser, SUserCreate, SUserUpdate
from app.users.service import UserService, provide_users_service


class UserController(Controller):
    path = "/users"
    dependencies = {"users_service": Provide(provide_users_service)}
    tags = ["Users"]

    @get()
    async def list_users(
        self,
        users_service: UserService,
    ) -> OffsetPagination[SUser]:
        """Получение всех пользователей."""
        results = await users_service.list()
        return users_service.to_schema(
            data=results,
            schema_type=SUser,
        )

    @post()
    async def create_user(
        self,
        users_service: UserService,
        data: SUserCreate,
    ) -> SUser:
        """Создание нового пользователя."""
        obj = await users_service.create(data)
        return users_service.to_schema(data=obj, schema_type=SUser)

    @get(path="/{user_id:int}")
    async def get_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(
            title="User ID",
            description="The user to retrieve.",
        ),
    ) -> SUser:
        """Получение конкретного пользователя."""
        obj = await users_service.get(user_id)
        return users_service.to_schema(data=obj, schema_type=SUser)

    @patch(path="/{user_id:int}")
    async def update_user(
        self,
        users_service: UserService,
        data: SUserUpdate,
        user_id: int = Parameter(
            title="User ID",
            description="The user to update.",
        ),
    ) -> SUser:
        """Обновление пользователя."""
        obj = await users_service.update(data=data, item_id=user_id)
        return users_service.to_schema(obj, schema_type=SUser)

    @delete(path="/{user_id:int}")
    async def delete_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(
            title="User ID",
            description="The user to delete.",
        ),
    ) -> None:
        """Удаление пользователя по его ID."""
        _ = await users_service.delete(user_id)
