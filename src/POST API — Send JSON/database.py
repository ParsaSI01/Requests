import sqlite3


class Database:
    def __init__(self,name_db):
        self.connection=sqlite3.connect(name_db)
        self.cursor=self.connection.cursor()
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS car_table (
                            title NVARCHAR(100) UNIQUE ,
                            kiloMetter NVARCHAR(100),
                            price NVARCHAR(100),
                            location NVARCHAR(150),
                            url NVARCHAR(100)
                            
                            );
        """)
    def insert_into_db(self,title,kiloometter,price,location,url):
        self.cursor.execute('INSERT OR IGNORE INTO car_table VALUES (?,?,?,?,?)',(title,kiloometter,price,location,url))
        self.connection.commit()