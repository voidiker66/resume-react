from sqlalchemy import create_engine
import json
import os
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
if os.path.exists("../../resumedb.db"):
	e = create_engine("sqlite:///../../resumedb.db")
	with open('../json/company_list.json', 'r') as json_data:
		d = json.load(json_data)
		givendata = d["data"]
		for i in givendata:
			company_name = i["company_name"]
			company_location = i["company_location"]
			company_contact = i["company_contact"]

			e.execute("""insert into Company(company_name, company_location, company_contact) values 
				(:company_name, :company_location, :company_contact)""", company_name=company_name,
				company_location=company_location, company_contact=company_contact)
else:
	sys.exit("Company Table Does Not Exist")








#if we wanted to insert multiple records into a table, a transaction would need to be created

#conn = engine.connect()
#trans = conn.begin()
#conn.execute("insert into parks (park_id) values ('YELL')")
#conn.execute("insert into parks (park_id) values ('ACAD')")
#trans.commit()
#conn.close()