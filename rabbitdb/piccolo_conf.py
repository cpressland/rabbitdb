"""Piccolo configuration file for RabbitDB."""

from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from rabbitdb import config

DB = PostgresEngine(config={"dsn": config.database_url})
APP_REGISTRY = AppRegistry(apps=["piccolo_admin.piccolo_app", "rabbitdb.piccolo_app"])
