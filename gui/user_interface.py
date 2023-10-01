from tkinter import *
from PIL import ImageTk, Image
from mysql_connector.connector import ConnectionToMySqlServer


my_connection = None

class StartDisplay:
    def __init__(self, master):
        self.login_button = None
        self.password_entry = None
        self.username_entry = None
        self.username_label = None
        self.password_label = None

        self.master = master
        self.master.title("PDF EXPORTER")

        self.frame = Frame(self.master, width=600, height=400, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        initial_image = (Image.open('C:\\Users\\Marius Murea\\Desktop\\Python\\SchoolManagement\\images\\school.png'))
        resized_image = initial_image.resize((500, 250))
        new_school_image = ImageTk.PhotoImage(resized_image)

        self.school_image = Label(self.frame, image=new_school_image, borderwidth=0, compound=CENTER)
        self.school_image.image = new_school_image
        self.school_image.place(x=75, y=0)

        self.log_in = Button(self.frame, text="Try to LOG IN", command=self.log_in_button_function,
                             activeforeground="#FFFFFF", activebackground="Green")
        self.log_in.place(x=250, y=300)
        self.log_in.configure(width=15, height=2)

    def log_in_button_function(self):
        self.log_in.destroy()

        self.username_label = Label(self.frame, text="Username: ", borderwidth=0, compound=CENTER, font=('Arial', 20))
        self.username_label.place(x=50, y=275)

        self.username_entry = Entry(self.frame, font=("Arial", 16), width=10)
        self.username_entry.place(x=200, y=280)

        self.password_label = Label(self.frame, text="Password: ", borderwidth=0, compound=CENTER,
                                    font=('Arial', 20))
        self.password_label.place(x=50, y=325)

        self.password_entry = Entry(self.frame, show="*", font=("Arial", 16), width=10)
        self.password_entry.place(x=200, y=330)

        self.login_button = Button(self.frame, text="Login", font=("Arial", 16), command=self.login)
        self.login_button.place(x=400, y=300)

        self.master.mainloop()

    def login(self):
        global my_connection
        my_connection = ConnectionToMySqlServer(self.username_entry.get(), self.password_entry.get())
        my_connection.connect_to_mysql_server()

        if my_connection.is_connected:
            self.master.destroy()
            self.master = Tk()
            self.app = CategoriesDisplay(self.master)
            self.master.mainloop()


class CategoriesDisplay:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF EXPORTER")
        self.master.geometry('600x500')

        self.frame = Frame(self.master, background='white', width=600, height=500, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        initial_image = (Image.open('C:\\Users\\Marius Murea\\Desktop\\Python\\SchoolManagement\\images\\school.png'))
        resized_image = initial_image.resize((500, 250))
        new_school_image = ImageTk.PhotoImage(resized_image)

        self.school_image = Label(self.frame, image=new_school_image, borderwidth=0, compound=CENTER,
                                  background='white')
        self.school_image.image = new_school_image
        self.school_image.place(x=75, y=0)

        self.categoria_clase = Button(self.frame, text='Clase', activebackground="Green",
                                      command=lambda: self.selected_category('Clase'))
        self.categoria_clase.config(font=("Courier bold", 16), width=7, height=1)
        self.categoria_clase.place(x=150, y=300)

        self.categoria_elevi = Button(self.frame, text='Elevi', activebackground="Green",
                                      command=lambda: self.selected_category('Elevi'))
        self.categoria_elevi.config(font=("Courier bold", 16), width=7, height=1)
        self.categoria_elevi.place(x=150, y=400)

        self.categoria_profesori = Button(self.frame, text='Profesori', activebackground="Green",
                                          command=lambda: self.selected_category('Profesori'))
        self.categoria_profesori.config(font=("Courier bold", 16), width=8, height=1)
        self.categoria_profesori.place(x=375, y=300)

        self.biblioteca = Button(self.frame, text='Biblioteca', activebackground="Green",
                                 command=lambda: self.selected_category('Biblioteca'))
        self.biblioteca.config(font=("Courier bold", 16), width=8, height=1)
        self.biblioteca.place(x=375, y=400)

        self.master.mainloop()

    def selected_category(self, category: str):
        self.master.destroy()

        if category == "Clase":
            self.master = Tk()
            self.app = Clase(self.master)

        self.master.mainloop()


class Clase:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF EXPORTER")
        self.master.geometry('600x500')

        self.frame = Frame(self.master, width=600, height=500, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        initial_image = (Image.open('C:\\Users\\Marius Murea\\Desktop\\Python\\SchoolManagement\\images\\school.png'))
        resized_image = initial_image.resize((500, 150))
        new_school_image = ImageTk.PhotoImage(resized_image)

        self.school_image = Label(self.frame, image=new_school_image, borderwidth=0, compound=CENTER)
        self.school_image.image = new_school_image
        self.school_image.place(x=75, y=0)

        self.class_id = Label(self.frame, text="ID: ", borderwidth=0, compound=CENTER, font=('Arial', 20))
        self.class_id.place(x=10, y=245)

        self.class_id_entry = Entry(self.frame, font=("Arial", 16), width=3)
        self.class_id_entry.place(x=60, y=250)

        self.class_name = Label(self.frame, text="Class Name: ", borderwidth=0, compound=CENTER, font=('Arial', 20))
        self.class_name.place(x=10, y=285)

        self.class_name_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.class_name_entry.place(x=170, y=290)

        self.number_of_students = Label(self.frame, text="Number Of Students: ", borderwidth=0, compound=CENTER, font=('Arial', 20))
        self.number_of_students.place(x=10, y=340)

        self.number_of_students_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.number_of_students_entry.place(x=270, y=345)

        self.average_grade = Label(self.frame, text="Average Grade: ", borderwidth=0, compound=CENTER,
                                        font=('Arial', 20))
        self.average_grade.place(x=10, y=390)

        self.average_grade_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.average_grade_entry.place(x=215, y=395)

        self.create_row_button = Button(self.frame, text="POST", font=("Arial", 16), command=self.create_row)
        self.create_row_button.place(x=400, y=300)

        self.master.mainloop()

    def create_row(self):
        my_connection.create_class_row(self.class_id_entry.get(), self.class_name_entry.get(),
                                       self.number_of_students_entry.get(), self.average_grade_entry.get())
