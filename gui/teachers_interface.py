from tkinter import *
from PIL import ImageTk, Image

import utility.pdf_functions as pdf
import gui.categories_interface


class Teachers:
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

        self.teacher_id = Label(self.frame, text="ID: ", borderwidth=0, compound=CENTER, font=('Arial', 20))
        self.teacher_id.place(x=10, y=245)

        self.teacher_id_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.teacher_id_entry.place(x=270, y=250)

        self.teacher_name = Label(self.frame, text="Teacher Name: ", borderwidth=0, compound=CENTER,
                                        font=('Arial', 20))
        self.teacher_name.place(x=10, y=325)

        self.teacher_name_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.teacher_name_entry.place(x=270, y=330)

        self.number_of_classes = Label(self.frame, text="Number of classes: ", borderwidth=0, compound=CENTER,
                              font=('Arial', 20))
        self.number_of_classes.place(x=10, y=390)

        self.number_of_classes_entry = Entry(self.frame, font=("Arial", 16), width=4)
        self.number_of_classes_entry.place(x=270, y=395)

        self.create_row_button = Button(self.frame, text="POST", font=("Arial", 16), command=self.create_row)
        self.create_row_button.place(x=400, y=300)

        self.get_information_button = Button(self.frame, text="GET", font=("Arial", 16), command=self.get_information)
        self.get_information_button.place(x=400, y=370)

        self.reset_table_button = Button(self.frame, text="RESET", font=("Arial", 16), command=self.reset_class_table)
        self.reset_table_button.place(x=400, y=250)

        self.back = Button(self.frame, text='Back', activebackground="Green", command=self.back_to_categories_display)
        self.back.config(font=("Courier bold", 16), width=5, height=1)
        self.back.place(x=10, y=25)

        self.master.mainloop()

    def create_row(self):
        self.my_connection.create_teacher(self.teacher_id_entry.get(), self.teacher_name_entry.get(), self.number_of_classes_entry.get())

        self.teacher_id_entry.delete(0, END)
        self.teacher_name_entry.delete(0, END)
        self.number_of_classes_entry.delete(0, END)

    def get_information(self):
        data = self.my_connection.get_data_from_table("Teachers")
        pdf.create_pdf(data, "Teachers")

    def reset_class_table(self):
        self.my_connection.reset_tables("Teachers")

    def back_to_categories_display(self):
        self.master.destroy()
        self.master = Tk()
        self.app = gui.categories_interface.CategoriesDisplay(self.master, self.my_connection)
        self.master.mainloop()
