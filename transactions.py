import sqlite3
import csv


class transactions:
    def __init__(self, db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        # itemNo becomes an alias of rowid column
        cur.execute('''CREATE TABLE IF NOT EXISTS Transactions(
                    itemNo INTEGER PRIMARY KEY, 
                    amount float, 
                    category text, 
                    date date, 
                    description text
                    )''')
        con.commit()
        con.close()
        self.db = db

    def select_one(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()

    # retrieves all transactions
    def select_all(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
