"""Import all routers and add them to routers_list."""
from .group import group_router
from .start import start_router


routers_list = [
    group_router,
    start_router,
]

__all__ = [
    "routers_list",
]
