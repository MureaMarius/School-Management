from tkinter import *
from PIL import ImageTk, Image

import gui.login_interface
from gui.classes_interface import Classes
from gui.students_interface import Students


class CategoriesDisplay:
    def __init__(self, master, my_connection):
        self.my_connection = my_connection
        self.master = master
        self.master.title("PDF EXPORTER")
        self.master.geometry('700x500')
        self.my_connection = my_connection

        self.frame = Frame(self.master, background='white', width=700, height=500, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        initial_image = (Image.open('C:\\Users\\Marius Murea\\Desktop\\Python\\SchoolManagement\\images\\school.png'))
        resized_image = initial_image.resize((600, 250))
        new_school_image = ImageTk.PhotoImage(resized_image)

        self.school_image = Label(self.frame, image=new_school_image, borderwidth=0, compound=CENTER,
                                  background='white')
        self.school_image.image = new_school_image
        self.school_image.place(x=75, y=0)

        self.category_classes = Button(self.frame, text='Classes', activebackground="Green",
                                      command=lambda: self.selected_category('Classes'))
        self.category_classes.config(font=("Courier bold", 16), width=7, height=1)
        self.category_classes.place(x=150, y=300)

        self.category_students = Button(self.frame, text='Students', activebackground="Green",
                                      command=lambda: self.selected_category('Students'))
        self.category_students.config(font=("Courier bold", 16), width=7, height=1)
        self.category_students.place(x=150, y=400)

        self.category_teachers = Button(self.frame, text='Teachers', activebackground="Green",
                                          command=lambda: self.selected_category('Teachers'))
        self.category_teachers.config(font=("Courier bold", 16), width=8, height=1)
        self.category_teachers.place(x=325, y=300)

        self.library = Button(self.frame, text='Library', activebackground="Green",
                                 command=lambda: self.selected_category('Library'))
        self.library.config(font=("Courier bold", 16), width=8, height=1)
        self.library.place(x=325, y=400)

        self.create_tables_button = Button(self.frame, text="Reset Database", activebackground="Green",
                                           command=self.reset_database)
        self.create_tables_button.config(font=("Courier bold", 16), width=13, height=1)
        self.create_tables_button.place(x=500, y=350)

        self.back = Button(self.frame, text='Back', activebackground="Green", command=self.back_to_login_display)
        self.back.config(font=("Courier bold", 16), width=7, height=1)
        self.back.place(x=10, y=25)

        self.master.mainloop()

    def selected_category(self, category: str):
        self.master.destroy()

        if category == "Classes":
            self.master = Tk()
            self.app = Classes(self.master, self.my_connection)
        elif category == "Students":
            self.master = Tk()
            self.app = Students(self.master, self.my_connection)
        elif category == "Teachers":
            pass

        self.master.mainloop()

    def reset_database(self):
        self.my_connection.create_tables_for_categories()

    def back_to_login_display(self):
        self.master.destroy()
        self.master = Tk()
        self.app = gui.login_interface.StartDisplay(self.master)
        self.master.mainloop()