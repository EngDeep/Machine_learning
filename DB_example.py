import MySQLdb

db = MySQLdb.connect(host="localhost", user="admin", passwd="admin123", db="test")

cur = db.cursor()

cur.execute("INSERT brass INTO db (ID,name.number)")
cur.commit()

cur.execute("SELECT * FROM YOUR_TABLE_NAME")


for row in cur.fetchall():
    print
    row[0]

db.close()
