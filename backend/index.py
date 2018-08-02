#!/usr/bin/env python

from flask import Flask,jsonify,request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumedb.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb'
db = SQLAlchemy(app)
CORS(app)
# mysql = MySQL()


class Company(db.Model):
    company_db_id = db.Column(db.Integer, primary_key = True)
    company_name = db.Column(db.String(32))
    company_location = db.Column(db.String(32))
    company_contact = db.Column(db.String(32))

class Project(db.Model):
    project_db_id = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(32))
    project_description = db.Column(db.String(200))
    project_languages = db.Column(db.String(100))
    project_work = db.Column(db.Integer)

class Work(db.Model):
    work_db_id = db.Column(db.Integer, primary_key = True)
    work_company = db.Column(db.Integer)
    work_job_title = db.Column(db.String(32))
    work_description = db.Column(db.String(200))
    work_start = db.Column(db.String(32))
    work_end = db.Column(db.String(32))

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well
manager.create_api(Company, methods=['GET'],results_per_page=15)
manager.create_api(Project, methods=['GET'],results_per_page=15)
manager.create_api(Work, methods=['GET'],results_per_page=15)

# app.config['MYSQL_DATABASE_USER'] = 'vcchau'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'parksareawesome'
# app.config['MYSQL_DATABASE_DB'] = 'parksareawesomedb'
# app.config['MYSQL_DATABASE_HOST'] = 'parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com'
# mysql.init_app(app)
# conn = mysql.connect()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
