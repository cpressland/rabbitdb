from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2024-11-08T18:09:40:924929"
VERSION = "1.22.0"
DESCRIPTION = "Initial Database"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="rabbitdb", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="Rabbit",
        tablename="rabbits",
        column_name="colour",
        db_column_name="colour",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 15,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
