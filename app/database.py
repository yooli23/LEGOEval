from db_by_josh.schema import Schema, Table, Column
from db_by_josh.store import Database as SQL


schema = Schema("database")

tasks = Table("task")
tasks.add_column("task_id", Column.TEXT)
tasks.add_column("state", Column.TEXT)
schema.add_table(tasks)

mturk = Table("mturk")
mturk.add_column("task_group_id", Column.TEXT)
mturk.add_column("hit_id", Column.TEXT)
mturk.add_column("complete", Column.INTEGER)
schema.add_table(mturk)

mturk = Table("task_to_hit")
mturk.add_column("task_id", Column.TEXT)
mturk.add_column("hit_id", Column.TEXT)
schema.add_table(mturk)

Database = SQL(schema)