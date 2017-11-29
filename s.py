from peewee import *
from playhouse.pool import PooledSqliteExtDatabase
import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('pandu.db')


c = conn.cursor()

c.execute('''CREATE TABLE Stocks1
(date text, trans text, symbol text, qty real, price real)''')

c.execute("INSERT INTO Stocks1 VALUES ('2006-01-05','BUY','RHAT',1000,35.14)")

symbol = 'RHAT'
c.execute("SELECT * FROM Stocks1 WHERE symbol = '%s'" % symbol)


t = ('RHAT',)
c.execute('SELECT * FROM Stocks1 WHERE symbol=?', t)


purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ('2006-09-09', 'SELL', 'MSFT', 900, 54.00)
            ]
c.executemany('INSERT INTO Stocks1 VALUES (?,?,?,?,?)', purchases)

c.execute("ALTER TABLE Stocks1 ADD COLUMN name text")

conn.commit()

conn.close()


db = PooledSqliteExtDatabase('stock.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    date = CharField()
    trans = CharField()
    symbol = CharField()
    qty = FloatField()
    price = FloatField()


User.create_table(True)

for path in User.select().where(User.qty == 1000):
    print path.path
