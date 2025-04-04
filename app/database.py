from litestar.plugins.sqlalchemy import (
    AlembicAsyncConfig,
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)

from app.config import get_db_url

session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=get_db_url(),
    before_send_handler="autocommit",
    session_config=session_config,
    create_all=True,
    alembic_config=AlembicAsyncConfig(
        script_location="./app/migrations/",
    ),
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)
