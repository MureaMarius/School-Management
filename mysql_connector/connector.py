from tkinter import messagebox

import mysql.connector
from mysql.connector import Error


class ConnectionToMySqlServer:
    def __init__(self, username: str, password: str):
        self.is_connected = 0
        self.username = username
        self.password = password
        self.connection = None

    def connect_to_mysql_server(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                database='my_db',
                                                user=self.username,
                                                password=self.password)
            if self.connection.is_connected():
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")
                self.is_connected = 1
        except Error as e:
            messagebox.showerror(title="Error", message="Invalid login.")

    def create_class_row(self, id: int, class_name: str, number_of_students: str, average_grade: str):
        command = ("INSERT INTO Clase (id, class_name, number_of_students, average_grade) VALUES({id}, '{class_name}', "
                   "'{number_of_students}', '{average_grade}')").format(id=id, class_name=class_name, number_of_students=number_of_students,
                                                                   average_grade=average_grade)

        if self.connection.is_connected():
            print(command)

            cursor = self.connection.cursor()
            cursor.execute(command)

            self.connection.commit()