import sqlite3

# Aichuk Tripura


def toDictionary(tran_tuple):
    ''' tran is a  transaction tuple (itemNo, amount, category, date, description)'''
    tran = {'rowid': tran_tuple[0], 'itemNo': tran_tuple[1], 'amount': tran_tuple[2],
            'category': tran_tuple[3], 'date': tran_tuple[4], 'description': tran_tuple[5]}
    return tran

# Aichuk Tripura


def toDictionaryList(tran_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [toDictionary(tran_tuple) for tran_tuple in tran_tuples]


class Transactions:
    def __init__(self, db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        # itemNo becomes an alias of rowid column
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions(
                    itemNo INTEGER, 
                    amount FLOAT, 
                    category TEXT, 
                    date DATE, 
                    description TEXT
                    )''')
        con.commit()
        con.close()
        self.db = db

    # Aichuk Tripura
    # retrieves all transactions
    def select_all(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT rowid, * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return toDictionaryList(tuples)

    # Ameer Rayan
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

    # Aichuk Tripura
    # Deletes transaction
    def delete(self, itemNo):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=?''', (itemNo))
        con.commit()
        con.close()

    # Aichuk Tripura
    # List total transactions by date (day to day) in asc. order
    def summarize_by_date(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute('''SELECT date, SUM(amount)
                       FROM transactions
                       GROUP BY date
                       ORDER BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return toDictionaryList(tuples)

    # Aichuk Tripura
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
        return toDictionaryList(tuples)

    # Aichuk Tripura
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
        return toDictionaryList(tuples)

    # Aichuk Tripura
    # Summarizes according to category
    def summarize_by_category(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute('''SELECT category, SUM(amount)
                       FROM transactions
                       GROUP BY category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return toDictionaryList(tuples)
