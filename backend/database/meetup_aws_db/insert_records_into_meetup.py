from sqlalchemy import create_engine
import json
import os
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
e = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")
with open('../../database_json/meetup_results.json', 'r') as json_data:
	d = json.load(json_data)
	givendata = d["data"]
	for i in givendata:
		meetup_title = i["name"]
		if "description" in i:
			meetup_summary = i["description"]
		else:
			meetup_summary = None
		if "image" in i:			
			meetup_image = i["image"]
		else:
			meetup_image = "https://pbs.twimg.com/profile_images/875701356849504256/x8t7RxeV_400x400.jpg"
		if "venue" in i:
			meetup_location = i["venue"]["address_1"]
			meetup_country = i["venue"]["country"]
			if "state" in i["venue"]:
				meetup_state = i["venue"]["state"]
			else:
				meetup_state = None
		else:
			meetup_location = None
			meetup_country = None
			meetup_state = None	
				
		if "group" in i:
			meetup_group = i["group"]["name"]
		else:
			meetup_group = None		
		print(meetup_title)
		e.execute("""insert into events(meetup_title, meetup_summary, meetup_image, meetup_location, 
				meetup_state, meetup_country, meetup_group) values (%s, %s, %s, %s, %s, %s, %s);""", 
				meetup_title, meetup_summary, meetup_image, meetup_location, meetup_state, meetup_country, meetup_group)









#if we wanted to insert multiple records into a table, a transaction would need to be created

#conn = engine.connect()
#trans = conn.begin()
#conn.execute("insert into parks (park_id) values ('YELL')")
#conn.execute("insert into parks (park_id) values ('ACAD')")
#trans.commit()
#conn.close()