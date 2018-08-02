from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../../resumedb.db"):
	delete_id_number = 4
	engine = create_engine("sqlite:///../../resumedb.db")


	result = engine.execute("select * from Work where Work_db_id=:number", number=delete_id_number)
	for row in result:
		#print(row)
		db_id = row[0]
		work_job_title = row[2]
		print("deleteing record: (" + str(db_id) + ", " + work_job_title + ")")


	engine.execute("""delete from Work where Work_db_id=:number""", 
		number=delete_id_number)
else:
	sys.exit("Work Table Does Not Exist")