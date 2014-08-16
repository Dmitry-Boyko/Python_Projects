__author__ = 'dmitryboyko'

import sqlite3 as db

conn = db.connect('test.db') # connection to database
cursor = conn.cursor()
cursor.execute("drop table if exists temps") # check if this table exist
cursor.execute("create table temps(date txt, temp int)") # create a table "temps" with two projections(columns)
cursor.execute('insert into temps values("12/1/2014", 35)') # insert data into table
cursor.execute('insert into temps values("12/2/2014", 42)')
cursor.execute('insert into temps values("12/3/2014", 38)')
cursor.execute('insert into temps values("12/4/2014", 41)')
cursor.execute('insert into temps values("12/5/2014", 40)')
cursor.execute('insert into temps values("12/6/2014", 38)')
cursor.execute('insert into temps values("12/7/2014", 45)')
conn.row_factory = db.Row # retrieving data
cursor.execute("select * from temps")
rows = cursor.fetchall()
for row in rows:
    print("%s %s" % (row[0], row[1]))
cursor.execute("select avg(temp) from temps") # compute average
row = cursor.fetchone()
print("The average temperature for the week was %s" and row[0])
cursor.execute("delete from temps where temp = 40") # delete a row
cursor.execute("select * from temps")
rows = cursor.fetchall()
for row in rows:
    print("%s %s" % (row[0], row[1]))
