from sqlalchemy import create_engine
import json
import os
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
if os.path.exists("../../resumedb.db"):
	e = create_engine("sqlite:///../../resumedb.db")
	with open('../json/work_list.json', 'r') as json_data:
		d = json.load(json_data)
		givendata = d["data"]
		for i in givendata:
			company = e.execute("select company_db_id from Company where company_name=\"" + i["work_company"] + "\"")
			x = -1
			for row in company:
				x = row["company_db_id"]
				break
			if x > 0:
				work_company = str(x)
			else:
				print("error: company not found")
				break
			work_job_title = i["work_job_title"]
			work_description = i["work_description"]
			work_start = i["work_start"]
			if i["work_end"]:
				work_end = i["work_end"]
			else:
				work_end = None

			e.execute("""insert into Work(work_company, work_job_title, work_description, work_start, work_end) values 
				(:work_company, :work_job_title, :work_description, :work_start, :work_end)""", work_company=work_company,
				work_job_title=work_job_title, work_description=work_description, work_start=work_start, work_end=work_end)
else:
	sys.exit("Work Table Does Not Exist")








#if we wanted to insert multiple records into a table, a transaction would need to be created

#conn = engine.connect()
#trans = conn.begin()
#conn.execute("insert into parks (park_id) values ('YELL')")
#conn.execute("insert into parks (park_id) values ('ACAD')")
#trans.commit()
#conn.close()