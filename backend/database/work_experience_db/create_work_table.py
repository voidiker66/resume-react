from sqlalchemy import create_engine
import os


e = create_engine("sqlite:///../../resumedb.db")

if os.path.exists("../../resumedb.db"):
	e.execute("""DROP TABLE IF EXISTS Work""")
e.execute("""
	create table Work (
		work_db_id integer primary key,
		work_company integer,
		work_job_title varchar,
		work_description varchar,
		work_start varchar,
		work_end varchar
	)
""")