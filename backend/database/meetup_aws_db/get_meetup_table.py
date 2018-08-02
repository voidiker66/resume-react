from sqlalchemy import create_engine
import os
import sys

engine = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")


result = engine.execute("select * from events;")

for row in result:
	db_id = row[0]
	if row[1] != None:
		meetup_title = row[1]
	else:
		meetup_title = "No title given"
	if row[2] != None:
		meetup_summary = row[2]
	else:
		meetup_summary = "No summary given"
	print("(" + str(db_id) + ", " + meetup_title + ", " + meetup_summary + ")")