import sqlite3
import csv


class transactions:
    def __init__(self, db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNo INT, amount FLOAT, category_t TEXT, date DATE, description TEXT)''')
        con.commit()
        con.close()
        self.db = db

    '''returns all the transactions'''

    def show_trans(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
