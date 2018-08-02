from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../../resumedb.db"):
	delete_id_number = 4
	engine = create_engine("sqlite:///../../resumedb.db")


	result = engine.execute("select * from Project where project_db_id=:number", number=delete_id_number)
	for row in result:
		#print(row)
		db_id = row[0]
		project_title = row[1]
		print("deleteing record: (" + str(db_id) + ", " + project_name + ")")

	engine.execute("""delete from Project where project_db_id=:number""", 
		number=delete_id_number)
else:
	sys.exit("Project Table Does Not Exist")