from mec_cadastrar_orc import *
from mec_ordem_serv import *


class TelaMecan:
    def __init__(self):
        # cores
        self.co1 = "#4682B4"
        self.co2 = "#000080"
        self.co3 = "#FFFFFF"
        self.fonte = "times new roman ce"

        # janela mecanico
        self.janela = Toplevel()
        self.janela.title("Mecânico")
        self.janela.geometry("500x500")
        self.janela.resizable(width=False, height=False)
        self.janela.configure(bg=self.co1)

        # logo
        self.logo = Label(self.janela, text="CARPRO", font=("magneto", 50, "bold"), bg=self.co1, fg=self.co3)
        self.logo.place(relx=0.15, rely=0.14, relwidth=0.7, relheight=0.2)

        # label mecânico
        self.mecanico_label = Label(self.janela, text="Mecânico", bg=self.co1, fg=self.co3, font=(self.fonte, 12, "bold"))
        self.mecanico_label.place(relx=0.43, rely=0.35)

        # botão cadastrar orçamento
        self.cadastrar_orcamento_btn = Button(self.janela, relief=FLAT,  text="Cadastrar orçamento", bd=3,
                                              font=(self.fonte, 12, "bold"), command=self.cadastrar_orcamento,
                                              fg=self.co1)
        self.cadastrar_orcamento_btn.place(relx=0.29, rely=0.45, relwidth=0.44)

        # botão ordem_servico_mecanico
        self.ordem_servico_mecanico = Button(self.janela, text="Ordens serviço", bd=3, relief=FLAT, fg=self.co1,
                                             font=(self.fonte, 12, "bold"), command=self.ordem_servico_mecanico)
        self.ordem_servico_mecanico.place(relx=0.29, rely=0.57, relwidth=0.44)

        # botão sair
        self.sair = Button(self.janela, text="Sair", bd=3, relief=FLAT, fg=self.co1,
                                             font=(self.fonte, 12, "bold"), command=self.janela.destroy)
        self.sair.place(relx=0.29, rely=0.69, relwidth=0.44)

        mainloop()

    def cadastrar_orcamento(self):
        tela = CadastroOrc()

    def ordem_servico_mecanico(self):
        tela = OrdemServicoMec()
