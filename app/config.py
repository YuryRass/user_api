from dotenv import dotenv_values

config = dotenv_values(".env")


def get_db_url() -> str:
    return (
        f"postgresql+asyncpg://{config['DB_USER']}:{config['DB_PASS']}@"
        f"{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"
    )
