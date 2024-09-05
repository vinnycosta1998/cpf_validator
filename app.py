from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.screen()
        self.frames()
        root.mainloop()

    def screen(self):
        self.root.configure(background="#000")
        self.root.geometry("240x240")
        self.root.resizable(False, False)
        self.root.title("CPF Validator")

    def frames(self):
        self.container = Frame(self.root, bg="#fff")
        self.container.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96) 

Application()