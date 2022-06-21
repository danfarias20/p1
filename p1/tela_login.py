from tkinter import *
from tela_gerente import *
from tela_mecanico import *
from tela_recepcionista import *
from db_funcionario import *


class Tela:
    def __init__(self):
        # cores
        self.co1 = "#00008B"
        self.co2 = "#000080"
        self.co3 = "#FFFFFF"
        self.fonte = "times new roman ce"

        # criando janela login
        self.janela_login = Tk()
        self.janela_login.geometry("500x500")
        self.janela_login.title("Login")
        self.janela_login.configure(bg=self.co1)
        self.janela_login.resizable(False, False)

        # logo
        self.logo = Label(self.janela_login, text="CARPRO", font=("magneto", 45, "bold"), bg=self.co1, fg=self.co3)
        self.logo.place(relx=0.15, rely=0.14, relwidth=0.7, relheight=0.2)

        # user
        self.user_label = Label(self.janela_login, text="Usuário: ", bg=self.co1, font=(self.fonte, 15, "bold"),
                                fg=self.co3)
        self.user_label.place(relx=0.3, rely=0.4)
        self.user_entry = Entry(self.janela_login, relief=FLAT)
        self.user_entry.place(relx=0.305, rely=0.47, relwidth=0.4, relheight=0.05)

        # senha
        self.senha_label = Label(self.janela_login, text="Senha: ", bg=self.co1, font=(self.fonte, 15, "bold"),
                                 fg=self.co3)
        self.senha_label.place(relx=0.3, rely=0.54)
        self.senha_entry = Entry(self.janela_login, width=30, show="*", relief=FLAT)
        self.senha_entry.place(relx=0.305, rely=0.62, relwidth=0.4, relheight=0.05)

        # botão entrar
        self.entrar_btn = Button(self.janela_login, text="Entrar", width=10, command=self.login, bd=3, relief=FLAT,
                                 font=(self.fonte, 15), fg=self.co1)
        self.entrar_btn.place(relx=0.405, rely=0.75, relwidth=0.2, relheight=0.07)

        # mensagem erro
        self.msg = Label(self.janela_login, text="", bg=self.co1, fg="red")
        self.msg.place(x=255, y=350)

        self.janela_login.mainloop()

    def login(self):
        user = self.user_entry.get()
        senha = self.senha_entry.get()
        db = sqlite3.connect("funcionarios.db")
        cursor = db.cursor()
        cursor.execute("SELECT cargo FROM funcionarios WHERE nome = '{}' AND senha = '{}'".format(user, senha))
        cargo_db = cursor.fetchall()
        db.close()
        if cargo_db[0][0] == "Gerente":
            tela = TelaGerente()
        elif cargo_db[0][0] == "Recepcionista":
            tela = TelaRecep()
        elif cargo_db[0][0] == "Mecânico":
            tela = TelaMecanico()
        else:
            self.msg["text"] = "Usuário e/ou senha incorretos"


tela = Tela()
