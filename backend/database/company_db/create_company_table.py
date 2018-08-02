from sqlalchemy import create_engine
import os


e = create_engine("sqlite:///../../resumedb.db")

if os.path.exists("../../resumedb.db"):
	e.execute("""DROP TABLE IF EXISTS Company""")
e.execute("""
	create table Company (
		company_db_id integer primary key,
		company_name varchar,
		company_location varchar,
		company_contact varchar
	)
""")