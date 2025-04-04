from litestar import Litestar

from app.database import alchemy
from app.users.controller import UserController

app = Litestar(route_handlers=[UserController], plugins=[alchemy])
