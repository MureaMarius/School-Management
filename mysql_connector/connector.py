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

    def create_class(self, id: int, class_name: str, number_of_students: str, average_grade: str):
        command = ("INSERT INTO Classes (id, class_name, number_of_students, average_grade) VALUES({id}, '{class_name}', "
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

    def create_teacher(self, id: int, teacher_name: str, number_of_classes: int):
        command = (
            "INSERT INTO Teachers (id, teacher_name, number_of_classes) VALUES({id}, '{teacher_name}', "
            "'{number_of_classes}')").format(id=id, teacher_name=teacher_name, number_of_classes=number_of_classes)

        if self.connection.is_connected():
            print(command)

            cursor = self.connection.cursor()
            cursor.execute(command)

            self.connection.commit()

    def get_data_from_table(self, category: str):
        select_command = f"SELECT * FROM {category}".format(category=category)

        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute(select_command)

            return cursor.fetchall()

    def reset_tables(self, category: str):
        drop_command = f"DROP TABLE {category}".format(category=category)

        if self.connection.is_connected():
            print(drop_command)

            cursor = self.connection.cursor()

            try:
                cursor.execute(drop_command)

                self.connection.commit()
            except mysql.connector.Error as e:
                print("Something went wrong: {}".format(e))

            if category == "Classes":
                cursor.execute(
                    "CREATE TABLE Classes (id int, class_name varchar(255), number_of_students int, average_grade float)")
            elif category == "Students":
                cursor.execute(
                    "CREATE TABLE Students (id int, student_first_name varchar(255), student_last_name varchar(255), absences int)")
            elif category == "Teachers":
                cursor.execute(
                    "CREATE TABLE Teachers (id int, teacher_name varchar(255), number_of_classes int)")
