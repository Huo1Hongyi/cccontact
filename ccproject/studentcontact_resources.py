import pymysql
from flask_sqlalchemy import SQLAlchemy

import os


class StudentContactResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user="admin",
            password="Hhy999626",
            host="database-3.citzedvikw2a.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM project_db.students where uni=%s";
        conn = StudentContactResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def add_user(uni, last_name, first_name, email):
        sql = "INSERT INTO project_db.students (uni, contact_name, email, tele) " \
              "VALUES (%s, %s, %s, %s)";
        conn = StudentContactResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=[uni, contact_name, email, tele])

        sql_check = "SELECT * FROM project_db.students where uni=%s";
        res = cur.execute(sql_check, args=uni)

        result = "Successfully added " + str(cur.fetchone())

        return result

