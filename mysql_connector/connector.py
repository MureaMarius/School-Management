from tkinter import messagebox

import mysql.connector
from mysql.connector import Error


class ConnectionToMySqlServer:
    def __init__(self, username: str, password: str):
        self.is_connected = 0
        self.username = username
        self.password = password

    def connect_to_mysql_server(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='my_db',
                                                user=self.username,
                                                password=self.password)
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")

                cursor = connection.cursor()
                """cursor.execute("select * from persons")
                record = cursor.fetchone()"""

                self.is_connected = 1
        except Error as e:
            messagebox.showerror(title="Error", message="Invalid login.")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
