import sqlite3

if __name__ == '__main__':
    with open('schema.sql', 'r') as f:
            query = f.read()
            
    with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.executescript(query)
            conn.commit()