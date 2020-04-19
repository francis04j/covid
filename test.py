import sqlite3

connection = sqlite3.connect('data.db') #data.db is the name of where we intend to store our data
cursor = connection.cursor()    #cursor is responsible for caccessing, stoting data in db, like a pointer

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

user = (1, 'Bob', 'pass')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'Jose', 'pass'),
    (3, 'Alice', 'pass')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * from users"
for row in cursor.execute(select_query):
    print (row)

connection.commit()

connection.close()  #so that it is not consuming resources while it waits for more data