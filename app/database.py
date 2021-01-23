from db_by_josh.schema import Schema, Table, Column
from db_by_josh.store import Database as SQL


schema = Schema("database")
tasks = Table("task")
tasks.add_column("task_id", Column.TEXT)
tasks.add_column("state", Column.TEXT)
schema.add_table(tasks)

Database = SQL(schema)