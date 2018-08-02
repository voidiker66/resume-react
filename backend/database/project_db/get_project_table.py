from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../../resumedb.db"):
	engine = create_engine("sqlite:///../../resumedb.db")


	result = engine.execute("select * from Project")
	#result = engine.execute("select * from "
	# "parks where park_name=:name", name='Yellowstone')

	for row in result:
		#print(row)
		db_id = row[0]
		project_name = row[1]
		project_description = row[2]
		project_languages = row[3]
		project_work = row[4]

		print(str(db_id) + ": " + project_name + ", " + project_description + ", " + project_languages + ", " + str(project_work) +"\n")
else:
	sys.exit("Project Table Does Not Exist")