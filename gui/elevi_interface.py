from tkinter import *
from PIL import ImageTk, Image


class Elevi:
    def __init__(self, master, my_connection):
        self.master = master
        self.master.title("PDF EXPORTER")
        self.master.geometry('600x500')
        self.my_connection = my_connection

        self.frame = Frame(self.master, width=600, height=500, relief=RAISED)
        self.frame.grid(row=0, column=0, sticky=NSEW)

        initial_image = (Image.open('C:\\Users\\Marius Murea\\Desktop\\Python\\SchoolManagement\\images\\school.png'))
        resized_image = initial_image.resize((500, 150))
        new_school_image = ImageTk.PhotoImage(resized_image)

        self.school_image = Label(self.frame, image=new_school_image, borderwidth=0, compound=CENTER)
        self.school_image.image = new_school_image
        self.school_image.place(x=75, y=0)
