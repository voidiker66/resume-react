from sqlalchemy import create_engine
import os


if os.path.exists("../../resumedb.db"):
	e = create_engine("sqlite:///../../resumedb.db")
	e.execute("""DROP TABLE IF EXISTS Project""")