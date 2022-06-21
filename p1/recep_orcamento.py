from tkinter import ttk
from db_ordem_orcamentos import *
from tkinter import *

# cores
co1 = "#D3D3D3"
co2 = "#000080"


class RecepOrcamentos:
    def __init__(self):
        def get_data(event):
            # pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
            selected_row = tv.focus()
            # pega o item(funcionário) que está nessa linha da tabela
            data = tv.item(selected_row)
            global row
            row = data["values"]

        def display_all():
            tv.delete(*tv.get_children())
            for i in db.fetch_orcamentos():
                tv.insert("", END, values=i)

        def del_orcamento():
            db.remove_orcamento(row[0])
            display_all()

        def transformar():
            db.trans_ordem(row[0])
            display_all()

        # cores
        co1 = "#D3D3D3"
        co2 = "#000080"
        fonte = "new times roman"
        db = Database("orcamentos.db")

        # janela orçamentos
        janela = Toplevel()
        janela.title("Cadastro orçamento")
        janela.geometry("900x500")
        janela.resizable(width=False, height=False)

        # criando frames
        frame_cima = Frame(janela, width=230, height=35, padx=1, bg=co2)
        frame_cima.grid(row=0, column=0, sticky=NSEW)

        frame_baixo = Frame(janela, width=230, height=400, padx=1)
        frame_baixo.grid(row=1, column=0, sticky=NSEW)

        frame_dir = Frame(janela, width=550, height=30, padx=1, bg=co1)
        frame_dir.grid(row=0, column=1, sticky=NSEW, rowspan=2)

        # titulo
        titulo = Label(frame_cima, text="Cadastro dos orçamentos", font=(fonte, 12), bg=co2, fg="white")
        titulo.place(x=4, y=10)

        # botão transformar
        transformar_btn = Button(frame_baixo, text="Transforma em ordem de serviço", command=transformar, width=27)
        transformar_btn.place(x=8, y=18)

        # botão excluir
        edit_btn = Button(frame_baixo, text="Excluir", command=del_orcamento, width=27)
        edit_btn.place(x=8, y=50)

        style = ttk.Style()
        style.configure("mystyle.Treeview", rowheight=30)
        style.configure("mystyle.Treeview.Heading")

        sb = Scrollbar(frame_dir)

        sb.pack(fill=Y, side=RIGHT)
        # Criando a tabela de fato
        tv = ttk.Treeview(frame_dir, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")
        tv.heading("1", text="Nª")
        tv.column("1", width=30, stretch=NO)
        tv.heading("2", text="CPF-Cliente")
        tv.column("2", width=150, stretch=NO)
        tv.heading("3", text="CPF-Mecanico")
        tv.column("3", width=150, stretch=NO)
        tv.heading("4", text="Valor")
        tv.column("4", width=80, stretch=NO)
        tv.heading("5", text="Descrição do Serviço")
        tv.column("5", width=240, stretch=NO)
        tv["show"] = "headings"
        tv.bind("<ButtonRelease-1>", get_data)
        tv.pack(fill=X)

        display_all()

        mainloop()

