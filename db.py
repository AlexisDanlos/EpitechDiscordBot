import sqlite3

# delete role col in loginlinks table

db = sqlite3.connect('dicord_bot\database.db')
c = db.cursor()
c.execute("ALTER TABLE loginlinks DROP COLUMN role")
db.commit()
db.close()
