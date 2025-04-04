from litestar.plugins.sqlalchemy import BigIntAuditBase
from sqlalchemy.orm import Mapped


class User(BigIntAuditBase):
    "Модель пользователей."
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]
