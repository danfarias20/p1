from tela_gerente import *
from tkinter import ttk
from db_ordem_orcamentos import *

# cores
co1 = "#D3D3D3"
co2 = "#000080"


class AdmOrdemServico:
    def __init__(self):
        def get_data(event):
            selected_row = tv.focus()

            data = tv.item(selected_row)
            global row
            row = data["values"]

        def display_all():
            tv.delete(*tv.get_children())
            for i in db.fetch_ordem():
                tv.insert("", END, values=i)

        def concluir():
            db.concluir_ordem(row[0])
            display_all()

        def remove():
            db.remove_ordem(row[0])
            display_all()

        def ver_concluidas():
            db.mostrar_concluidas()

        # cores
        co1 = "#D3D3D3"
        co2 = "#000080"
        fonte = "new times roman"

        db = Database("orcamentos.db")

        # janela ordens de serviços
        janela = Toplevel()
        janela.title("Ordens de serviços")
        janela.geometry("1000x500")
        janela.resizable(width=False, height=False)

        # criando frames
        frame_cima = Frame(janela, width=230, height=45, padx=1, bg=co2)
        frame_cima.grid(row=0, column=0, sticky=NSEW)

        frame_baixo = Frame(janela, width=230, height=400, padx=1)
        frame_baixo.grid(row=1, column=0, sticky=NSEW)

        frame_dir = Frame(janela, width=650, height=30, padx=1, bg=co1)
        frame_dir.grid(row=0, column=1, sticky=NSEW, rowspan=2)

        # titulo
        titulo = Label(frame_cima, text="Ordens de serviços", font=(fonte, 12), bg=co2, fg="white")
        titulo.place(x=10, y=10)

        # botão concluir ordem
        concluir_btn = Button(frame_baixo, text="Concluir", command=concluir, width=27)
        concluir_btn.place(x=8, y=15)

        # botão deletar ordem
        del_btn = Button(frame_baixo, text="Excluir", command=remove, width=27)
        del_btn.place(x=8, y=45)

        style = ttk.Style()
        style.configure("mystyle.Treeview", rowheight=30)
        style.configure("mystyle.Treeview.Heading")

        sb = Scrollbar(frame_dir)

        sb.pack(fill=Y, side=RIGHT)
        # Criando a tabela de fato
        tv = ttk.Treeview(frame_dir, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
        tv.heading("1", text="ID")
        tv.column("1", width=25, stretch=NO)
        tv.heading("2", text="CPF do cliente")
        tv.column("2", width=150, stretch=NO)
        tv.heading("3", text="CPF do mecânico")
        tv.column("3", width=150, stretch=NO)
        tv.heading("4", text="Valor")
        tv.column("4", width=150, stretch=NO)
        tv.heading("5", text="Descrição")
        tv.column("5", width=160, stretch=NO)
        tv.heading("6", text="Status")
        tv.column("6", width=115, stretch=NO)
        tv["show"] = "headings"
        tv.bind("<ButtonRelease-1>", get_data)
        tv.pack(fill=X)

        display_all()

        mainloop()
