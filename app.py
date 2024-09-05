from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.screen()
        root.mainloop()

    def screen(self):
        self.root.configure(background="#000")
        self.root.geometry("240x240")
        self.root.resizable(False, False)
        self.root.title("CPF Validator")

Application()