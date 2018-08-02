from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../../resumedb.db"):
	engine = create_engine("sqlite:///../../resumedb.db")


	result = engine.execute("select * from Work")
	#result = engine.execute("select * from "
	# "parks where park_name=:name", name='Yellowstone')

	for row in result:
		#print(row)
		db_id = row[0]
		c = engine.execute("select company_name from Company where company_db_id=\"" + str(row[1]) + "\"")
		for item in c:
			x = item["company_name"]
			break
		if x:
			company = x
		else:
			company = None
		job_title = row[2]
		description = row[3]
		start = row[4]
		end = row[5]

		print(str(db_id) + "\n" + company + "\n" + job_title + "\n" + description + "\n" + start + "\n" + end + "\n")
else:
	sys.exit("Work Table Does Not Exist")