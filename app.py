from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.screen()
        self.frames()
        self.buttons()
        root.mainloop()

    def screen(self):
        self.root.configure(background="#000")
        self.root.geometry("240x240")
        self.root.resizable(False, False)
        self.root.title("CPF Validator")

    def frames(self):
        self.container = Frame(self.root)
        self.container.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96) 

    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Selecione um arquivo Excel",
            filetypes=["Arquivos Excel", "*.xls *.xlsx"]
        )

        if self.file_path:
            messagebox.showinfo("Arquivo Selecionado", f"Arquivo selecionado, ${self.file_path}")
        else:
            messagebox.showinfo("Nenhum arquivo sleecionado", "Nenhum arquivo foi selecionado")
    
    def buttons(self):
        self.button_open_file = Button(self.container, text="Selecione um arquivo Excel", command=self.select_file)
        self.button_open_file.place(relx=0.05, rely=0.4, relwidth=0.90, relheight=0.15)


Application()