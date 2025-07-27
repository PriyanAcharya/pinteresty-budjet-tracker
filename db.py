import sqlite3

def init_db():
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item TEXT,
                    amount REAL,
                    category TEXT,
                    date TEXT
                )''')
    conn.commit()
    conn.close()

def add_expense(item, amount, category, date):
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (item, amount, category, date) VALUES (?, ?, ?, ?)",
              (item, amount, category, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect('budget.db')
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df
