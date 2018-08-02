from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../../resumedb.db"):
	engine = create_engine("sqlite:///../../resumedb.db")


	result = engine.execute("select * from Company")
	#result = engine.execute("select * from "
	# "parks where park_name=:name", name='Yellowstone')

	for row in result:
		#print(row)
		db_id = row[0]
		name = row[1]
		location = row[2]
		contact = row[3]

		print(str(db_id) + ": " + name + ", " + location + ", " + contact + "\n")
else:
	sys.exit("Company Table Does Not Exist")