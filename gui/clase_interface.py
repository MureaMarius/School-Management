from tkinter import *
from PIL import ImageTk, Image


class Clase:
    def __init__(self, master, my_connection):
        self.master = master
        self.master.title("PDF EXPORTER")
        self.master.geometry('600x500')
        self.my_connection = my_connection

        self.frame = Frame(self.master, width=600, height=500, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        initial_image = (Image.open('C:\\Users\\Marius Murea\\Desktop\\Python\\SchoolManagement\\images\\school.png'))
        resized_image = initial_image.resize((500, 200))
        new_school_image = ImageTk.PhotoImage(resized_image)

        self.school_image = Label(self.frame, image=new_school_image, borderwidth=0, compound=CENTER)
        self.school_image.image = new_school_image
        self.school_image.place(x=75, y=0)

        self.class_id = Label(self.frame, text="ID: ", borderwidth=0, compound=CENTER, font=('Arial', 20))
        self.class_id.place(x=10, y=245)

        self.class_id_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.class_id_entry.place(x=270, y=250)

        self.class_name = Label(self.frame, text="Class Name: ", borderwidth=0, compound=CENTER, font=('Arial', 20))
        self.class_name.place(x=10, y=285)

        self.class_name_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.class_name_entry.place(x=270, y=290)

        self.number_of_students = Label(self.frame, text="Number Of Students: ", borderwidth=0, compound=CENTER,
                                        font=('Arial', 20))
        self.number_of_students.place(x=10, y=340)

        self.number_of_students_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.number_of_students_entry.place(x=270, y=345)

        self.average_grade = Label(self.frame, text="Average Grade: ", borderwidth=0, compound=CENTER,
                                   font=('Arial', 20))
        self.average_grade.place(x=10, y=390)

        self.average_grade_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.average_grade_entry.place(x=270, y=395)

        self.create_row_button = Button(self.frame, text="POST", font=("Arial", 16), command=self.create_row)
        self.create_row_button.place(x=400, y=300)

        self.get_information_button = Button(self.frame, text="GET", font=("Arial", 16), command=self.get_information)
        self.get_information_button.place(x=400, y=370)

        self.master.mainloop()

    def create_row(self):
        self.my_connection.create_class(self.class_id_entry.get(), self.class_name_entry.get(),
                                        self.number_of_students_entry.get(), self.average_grade_entry.get())

        self.class_id_entry.delete(0, END)
        self.class_name_entry.delete(0, END)
        self.number_of_students_entry.delete(0, END)
        self.average_grade_entry.delete(0, END)

    def get_information(self):
        return None
