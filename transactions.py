import sqlite3
import csv


class transactions:
    def __init__(self, db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        # itemNo becomes an alias of rowid column
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions(
                    itemNo INTEGER PRIMARY KEY, 
                    amount float, 
                    category text, 
                    date date, 
                    description text
                    )''')
        con.commit()
        con.close()
        self.db = db

    def select_one(self, itemNo):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * from transactions where itemNo=(?)", (itemNo))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict(tuples[0])

    # retrieves all transactions
    def select_all(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()

    # Adds transaction
    def add(self, item):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",
                    (item['itemNo'], item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    # Deletes transaction
    def delete(self, itemNo):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE itemNo=(?)''', (itemNo))
        con.commit()
        con.close()

    # List total transactions by date (day to day) in asc. order
    def summarize_by_date(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute('''SELECT date, SUM(amount)
                       FROM transactions
                       GROUP BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_transactions_dict_list(tuples)

    # List total transactions by month in asc. order
    def summarize_by_month(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute('''SELECT strftime('%m', date) as Month, SUM(amount)
                       FROM transactions
                       GROUP BY strftime('%m', date)
                       ORDER BY strftime('%m', date)''')
        tuples = cur.fetchall()
        con.commit()
        con.close()

    # List total transactions by year in asc. order
    def summarize_by_year(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute('''SELECT strftime('%Y', date) as Year, SUM(amount)
                       FROM transactions
                       GROUP BY strftime('%Y', date)
                       ORDER BY strftime('%Y', date)''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
