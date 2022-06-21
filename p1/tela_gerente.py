from ger_gerenc_func import *
from ger_ordens_servico import *
from ger_ver_clientes import *


class TelaGerente:
    def __init__(self):
        # cores
        self.co1 = "#00008B"
        self.co2 = "#000080"
        self.co3 = "#FFFFFF"
        self.fonte = "times new roman ce"

        # janela recepcionista
        self.janela = Toplevel()
        self.janela.title("Gerente")
        self.janela.geometry("500x500")
        self.janela.resizable(width=False, height=False)
        self.janela.configure(bg=self.co1)

        # logo
        self.logo = Label(self.janela, text="CARPRO", font=("magneto", 50, "bold"), bg=self.co1, fg=self.co3)
        self.logo.place(relx=0.15, rely=0.14, relwidth=0.7, relheight=0.2)

        # label gerente
        self.gerente_label = Label(self.janela, text="Gerente", bg=self.co1, fg=self.co3,
                                 font=(self.fonte, 12, "bold"))
        self.gerente_label.place(relx=0.4, rely=0.35)

        # botão gerenciar funcionarios
        self.gerenc_func_btn = Button(self.janela, relief=FLAT,  text="Gerenciar Funcionários", bd=3,
                                      font=(self.fonte, 12, "bold"), command=self.gerec_func, fg=self.co1)
        self.gerenc_func_btn.place(relx=0.29, rely=0.45, relwidth=0.44)

        # botão ordens de serviço
        self.ordem_servico_btn = Button(self.janela, text="Ordens de serviço", bd=3, relief=FLAT, fg=self.co1,
                                        font=(self.fonte, 12, "bold"), command=self.ordens_servico)
        self.ordem_servico_btn.place(relx=0.29, rely=0.57, relwidth=0.44)

        # botão clientes
        self.clientes_btn = Button(self.janela, text="Clientes", bd=3, relief=FLAT, fg=self.co1,
                                   font=(self.fonte, 12, "bold"), command=self.ver_clientes)
        self.clientes_btn.place(relx=0.29, rely=0.69, relwidth=0.44)

        # botão sair
        self.sair = Button(self.janela, text="Sair", bd=3, relief=FLAT, fg=self.co1, font=(self.fonte, 12, "bold"),
                           command=self.janela.destroy)
        self.sair.place(relx=0.29, rely=0.80, relwidth=0.44)

        mainloop()

    def gerec_func(self):
        tela = GerenteFunc()

    def ordens_servico(self):
        tela = AdmOrdemServico()

    def ver_clientes(self):
        tela = VerClientes()
