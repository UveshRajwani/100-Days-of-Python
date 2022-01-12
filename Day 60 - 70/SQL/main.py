import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE users(
#     first_name text,
#     last_name text,
#     email text
# )""")
# all_users = [
#     ('kal', 'brown', 'hahah@fg.kc'),
#     ('kal1', 'brown1', '1hahah@fg.kc'),
#     ('kal11', 'brown11', '11hahah@fg.kc'),
# ]
# cursor.execute("INSERT INTO users VALUES (?,?,?)", all_users)
# cursor.execute("INSERT INTO users VALUES ('funny','bot','funny@bot.com')")
cursor.execute("SELECT * FROM users")
# cursor.fetchone()
# cursor.fetchmany()
print(cursor.fetchall())

conn.commit()
conn.close()
