import sqlite3
con = sqlite3.connect("cc_db.db")
print(con)
cur = con.cursor()
print(cur)
res = cur.execute('''CREATE TABLE IF NOT EXISTS user (
                                        username text NOT NULL PRIMARY KEY,
                                        email text NOT NULL,
                                        password text NOT NULL,
                                        firstname text NOT NULL,                                        
                                        lastname text NOT NULL)''')
print(res.fetchall())

