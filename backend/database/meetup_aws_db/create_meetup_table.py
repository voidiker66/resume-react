
from sqlalchemy import create_engine


e = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")

e.execute("""
	create table events (
		events_db_id INT NOT NULL AUTO_INCREMENT,
		meetup_title VARCHAR(100),
		meetup_summary VARCHAR(1000),
		meetup_image VARCHAR(100),
		meetup_location VARCHAR(100),
		meetup_state VARCHAR(100),
		meetup_country VARCHAR(100),
		meetup_group VARCHAR(100),		
		primary key (events_db_id)
	);
""")