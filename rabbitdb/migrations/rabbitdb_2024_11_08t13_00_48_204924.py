from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Date
from piccolo.columns.defaults.date import DateNow
from piccolo.columns.indexes import IndexMethod


ID = "2024-11-08T13:00:48:204924"
VERSION = "1.22.0"
DESCRIPTION = "Initial Database"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="rabbitdb", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="Vaccinations",
        tablename="vaccinations",
        column_name="expires",
        db_column_name="expires",
        column_class_name="Date",
        column_class=Date,
        params={
            "default": DateNow(),
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
