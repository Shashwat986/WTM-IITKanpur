import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

purchases = (
    ('2006-01-05','BUY','RHAT',100,35.14),
    ('2006-01-12','SELL','IBM',20,154.28),
    ('2006-01-25','SELL','MSFT',130,41.38),
    ('2006-02-06','BUY','GOOG',10,547.32),
    ('2006-02-23','SELL','AAPL',40,123.59),
    ('2006-04-01','BUY','LNKD',10,259.12)
)

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

c.execute('SELECT * FROM stocks WHERE symbol=?', ('GOOG',))
print c.fetchone()

conn.commit()
conn.close()