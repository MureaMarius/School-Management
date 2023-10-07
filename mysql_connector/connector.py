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

    def create_tables_for_categories(self):
        clase_table = "CREATE TABLE Clase (id int PRIMARY KEY, class_name varchar(255), number_of_students int, average_grade float);"
        student_table = "CREATE TABLE Student (id int PRIMARY KEY, student_first_name varchar(255), student_last_name varchar(255), absences int);"
        profesori_table = "CREATE TABLE Profesori (id int PRIMARY KEY, last_name varchar(255), number_of_classes int);"

        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute("DROP TABLE Clase;")
            cursor.execute("DROP TABLE Student;")
            cursor.execute("DROP TABLE Profesori;")

            cursor.execute(clase_table)
            cursor.execute(student_table)
            cursor.execute(profesori_table)

            self.connection.commit()

    def create_class(self, id: int, class_name: str, number_of_students: str, average_grade: str):
        command = ("INSERT INTO Clase (id, class_name, number_of_students, average_grade) VALUES({id}, '{class_name}', "
                   "'{number_of_students}', '{average_grade}')").format(id=id, class_name=class_name,
                                                                        number_of_students=number_of_students,
                                                                        average_grade=average_grade)

        if self.connection.is_connected():
            print(command)

            cursor = self.connection.cursor()
            cursor.execute(command)

            self.connection.commit()

    def create_student(self, id: int, student_first_name: str, student_last_name: str, absences: int):
        command = (
            "INSERT INTO Students (id, student_first_name, student_last_name, absences) VALUES({id}, '{student_first_name}', "
            "'{student_last_name}', '{absences}')").format(id=id, student_first_name=student_first_name,
                                                           student_last_name=student_last_name,
                                                           absences=absences)

        if self.connection.is_connected():
            print(command)

            cursor = self.connection.cursor()
            cursor.execute(command)

            self.connection.commit()
