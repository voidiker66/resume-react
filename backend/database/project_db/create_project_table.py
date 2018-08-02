from sqlalchemy import create_engine
import os


e = create_engine("sqlite:///../../resumedb.db")

if os.path.exists("../../resumedb.db"):
	e.execute("""DROP TABLE IF EXISTS Project""")
e.execute("""
	create table Project (
		project_db_id integer primary key,
		project_name varchar,
		project_description varchar,
		project_languages varchar,
		project_work integer
	)
""")