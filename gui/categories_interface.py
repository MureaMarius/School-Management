from tkinter import *
from PIL import ImageTk, Image

from gui.clase_interface import Clase
from gui.elevi_interface import Elevi


class CategoriesDisplay:
    def __init__(self, master, my_connection):
        self.master = master
        self.master.title("PDF EXPORTER")
        self.master.geometry('600x500')
        self.my_connection = my_connection

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
            self.app = Clase(self.master, self.my_connection)
        elif category == "Elevi":
            self.master = Tk()
            self.app = Elevi(self.master, self.my_connection)

        self.master.mainloop()
