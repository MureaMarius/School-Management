from tkinter import *
from PIL import ImageTk, Image

from gui.categories_interface import CategoriesDisplay
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

        self.frame = Frame(self.master, width=700, height=400, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        initial_image = (Image.open('C:\\Users\\Marius Murea\\Desktop\\Python\\SchoolManagement\\images\\school.png'))
        resized_image = initial_image.resize((600, 250))
        new_school_image = ImageTk.PhotoImage(resized_image)

        self.school_image = Label(self.frame, image=new_school_image, borderwidth=0, compound=CENTER)
        self.school_image.image = new_school_image
        self.school_image.place(x=75, y=0)

        self.log_in = Button(self.frame, text="Try to LOG IN", command=self.log_in_button_function,
                             activeforeground="#FFFFFF", activebackground="Green")
        self.log_in.place(x=300, y=300)
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
            self.app = CategoriesDisplay(self.master, my_connection)
            self.master.mainloop()