from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class SUser(BaseSchema):
    """Схема пользователя для GET запросов."""

    id: int
    name: str
    surname: str
    password: str
    created_at: datetime
    updated_at: datetime


class SUserCreate(BaseSchema):
    """Схема для создания пользователей."""

    name: str
    surname: str
    password: str


class SUserUpdate(BaseSchema):
    """Схема для обновления пользователей."""

    name: str | None = None
    surname: str | None = None
    password: str | None = None
