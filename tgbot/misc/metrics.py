import datetime
from zoneinfo import ZoneInfo

from influxdb_client import WritePrecision, Point
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from infrastructure.database.models import User


async def log_stat(client: InfluxDBClientAsync, user: User, action: str):
    """Логирует действия пользователя в InfluxDB."""
    pass

async def stat_add_total(client: InfluxDBClientAsync, user: User, action: str):
    """Фиксирует добавление напоминаний в статистике."""
    pass

async def stat_sent_total(client: InfluxDBClientAsync, user: User | dict, action: str):
    """Фиксирует отправленные напоминания в статистике."""
    pass
