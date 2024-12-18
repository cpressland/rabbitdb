from piccolo_admin.endpoints import TableConfig

from rabbitdb.tables import Rabbit

rabbit = TableConfig(
    table_class=Rabbit,
    rich_text_columns=[Rabbit.notes],
    # link_column=Rabbit.name, # Causes form not to load for some reason.
)
