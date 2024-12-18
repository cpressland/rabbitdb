"""Piccolo App Config."""

from piccolo.conf.apps import AppConfig, Command, table_finder

from rabbitdb import server

APP_CONFIG = AppConfig(
    app_name="rabbitdb",
    migrations_folder_path="rabbitdb/migrations",
    table_classes=table_finder(["rabbitdb.tables"], exclude_imported=True),
    migration_dependencies=[],
    commands=[
        Command(callable=server, aliases=["run"]),
    ],
)
