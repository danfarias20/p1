from recep_cadastrar_cli import *
from recep_orcamento import *


class TelaRecep:
    def __init__(self):
        # cores
        self.co1 = "#00008B"
        self.co2 = "#000080"
        self.co3 = "#FFFFFF"
        self.fonte = "times new roman ce"

        # janela recepcionista
        self.janela = Toplevel()
        self.janela.title("Recepcionista")
        self.janela.geometry("500x500")
        self.janela.resizable(width=False, height=False)
        self.janela.configure(bg=self.co1)

        # logo
        self.logo = Label(self.janela, text="CARPRO", font=("magneto", 50, "bold"), bg=self.co1, fg=self.co3)
        self.logo.place(relx=0.15, rely=0.14, relwidth=0.7, relheight=0.2)

        # label recepcionista
        self.recep_label = Label(self.janela, text="Recepcionista", bg=self.co1, fg=self.co3,
                                 font=(self.fonte, 12, "bold"))
        self.recep_label.place(relx=0.4, rely=0.35)

        # botão cadastrar orçamento
        self.cadastrar_cli_btn = Button(self.janela, relief=FLAT,  text="Cadastrar Cliente", bd=3,
                                        font=(self.fonte, 12, "bold"), command=self.cadastrar_clientes, fg=self.co1)
        self.cadastrar_cli_btn.place(relx=0.29, rely=0.45, relwidth=0.44)

        # botão orçamentos
        self.orcamentos_btn = Button(self.janela, text="Orçamentos", bd=3, relief=FLAT, fg=self.co1,
                                     font=(self.fonte, 12, "bold"), command=self.orcamentos)
        self.orcamentos_btn.place(relx=0.29, rely=0.57, relwidth=0.44)

        # botão sair
        self.sair = Button(self.janela, text="Sair", bd=3, relief=FLAT, fg=self.co1,
                                             font=(self.fonte, 12, "bold"), command=self.janela.destroy)
        self.sair.place(relx=0.29, rely=0.69, relwidth=0.44)

        mainloop()

    def cadastrar_clientes(self):
        tela = CadastrarClientes()

    def orcamentos(self):
        tela = RecepOrcamentos()
