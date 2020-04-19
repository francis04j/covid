import sqlite3

class User:
    TABLE_NAME = 'users'

    def __init__(self,_id, username, password):
        self.id = _id
        self.username=username
        self.password=password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        # query = "SELECT * FROM users where username=?"
        result = cursor.execute(query, (username,)) #paramter have to be of type tuple hence comma to create single value tuple
        row = result.fetchone()
        if row:
            # user=User(row[0],row[1],row[2]) use cls rather than hardcoding class name User
            user = cls(*row)    #row expand to be the same thing
            
        else:
            user = None

        connection.close()
        return user
    
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user