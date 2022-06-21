from tkinter import messagebox
from tela_mecanico import *
from tkinter import ttk
from db_ordem_orcamentos import *
from db_funcionario import *
from tela_login import *
# cores
co1 = "#D3D3D3"
co2 = "#000080"


class OrdemServicoMec:
    def __init__(self):
        def getData(event):
            # pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
            selected_row = tv.focus()
            # pega o item(funcionário) que está nessa linha da tabela
            data = tv.item(selected_row)
            global row
            row = data["values"]

        def display_all():
            tv.delete(*tv.get_children())
            for i in db.fetch_ordem_mec(cpf_mecanico):
                tv.insert("", END, values=i)

        # cores
        co1 = "#D3D3D3"
        co2 = "#000080"
        fonte = "new times roman"

        nome = Tela.user()
        senha = Tela.senha()

        db = Database("orcamentos.db")
        con = sqlite3.connect("funcionarios.db")
        cursor = con.cursor()
        cursor.execute("SELECT cpf FROM funcionarios WHERE nome = ? and senha = ?", (nome, senha))
        cpf_mecanico = cursor.fetchall()

        # janela gerenciamento de funcionários
        janela = Toplevel()
        janela.title("Ordens de serviço")
        janela.geometry("900x500")
        janela.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("mystyle.Treeview", rowheight=30)
        style.configure("mystyle.Treeview.Heading")

        sb = Scrollbar(janela)

        sb.pack(fill=Y, side=RIGHT)
        # Criando a tabela de fato
        tv = ttk.Treeview(janela, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")
        tv.heading("1", text="Nª")
        tv.column("1", width=30, stretch=NO)
        tv.heading("2", text="CPF-Cliente")
        tv.column("2", width=150, stretch=NO)
        tv.heading("3", text="CPF-Mecanico")
        tv.column("3", width=150, stretch=NO)
        tv.heading("4", text="Valor")
        tv.column("4", width=50, stretch=NO)
        tv.heading("5", text="Descricao do Servico")
        tv.column("5", width=300, stretch=NO)
        tv["show"] = "headings"
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill=X)

        display_all()

        mainloop()
