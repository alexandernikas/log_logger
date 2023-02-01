import sqlite3
import pandas as pd

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS stools (id INTEGER PRIMARY KEY, length float, girth float, vol text, bristol int, date text, tags text)")
        self.conn.commit()
#        global stls
#        stls = pd.read_sql_query("SELECT * from stools", self.conn)


    def fetch(self):
        self.cur.execute("SELECT * FROM stools")
        rows = self.cur.fetchall()
        return rows

    def insert(self, length, girth, vol, bristol, date, tags):
        self.cur.execute("INSERT INTO stools VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (length, girth, vol, bristol, date, tags))
        self.conn.commit()

    def clear_db(self):
        self.cur.execute("DROP TABLE stools")

    def filter_table(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    
    def delete_row(self,row):
        query = "delete from stools where id =" + str(row)
        self.cur.execute(query)
        self.conn.commit()




#class Filter:
#    def __init__(self, db, query):
#        self.conn = sqlite3.connect(db)
#        self.cur = self.conn.cursor()
#        global fTable
#        fTable = pd.read_sql_query(query, self.conn)

