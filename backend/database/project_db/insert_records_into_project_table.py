from sqlalchemy import create_engine
import json
import os
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
if os.path.exists("../../resumedb.db"):
	e = create_engine("sqlite:///../../resumedb.db")
	with open('../json/project_list.json', 'r') as json_data:
		d = json.load(json_data)
		givendata = d["data"]
		for i in givendata:
			company = e.execute("select work_db_id from Work where work_company in (select company_db_id from Company where company_name=\"" + i["project_work"] + "\")")
			x = -1
			for row in company:
				x = row["work_db_id"]
				break
			if x > 0:
				project_work = str(x)
			else:
				print("error: company not found")
				break
			project_name = i["project_name"]
			project_description = i["project_description"]
			project_languages = i["project_languages"]

			e.execute("""insert into Project(project_name, project_description, project_languages, project_work) values 
				(:project_name, :project_description, :project_languages, :project_work)""", project_name=project_name,
				project_description=project_description, project_languages=project_languages, project_work=project_work)
else:
	sys.exit("Project Table Does Not Exist")









#if we wanted to insert multiple records into a table, a transaction would need to be created

#conn = engine.connect()
#trans = conn.begin()
#conn.execute("insert into parks (park_id) values ('YELL')")
#conn.execute("insert into parks (park_id) values ('ACAD')")
#trans.commit()
#conn.close()