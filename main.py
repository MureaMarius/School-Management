from tkinter import Tk
from gui.login_interface import StartDisplay


def main():
    root = Tk()
    app = StartDisplay(root)
    root.mainloop()


if __name__ == "__main__":
    main()
