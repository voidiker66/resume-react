from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../../resumedb.db"):
	delete_id_number = 4
	engine = create_engine("sqlite:///../../resumedb.db")


	result = engine.execute("select * from Company where company_db_id=:number", number=delete_id_number)
	for row in result:
		#print(row)
		db_id = row[0]
		wiki_title = row[1]
		print("deleteing record: (" + str(db_id) + ", " + wiki_title + ")")

	park_value = 'YELL'
	engine.execute("""delete from Company where wiki_db_id=:number""", 
		number=delete_id_number)
else:
	sys.exit("Company Table Does Not Exist")