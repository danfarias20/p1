from tkinter import messagebox
from tela_mecanico import *
from tkinter import ttk
from db_ordem_orcamentos import *
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
            cpfCliente.set(row[1])
            cpfMecanico.set(row[2])
            valor.set(row[3])
            descricaoDoServico.set(row[4])

        def displayAll():
            tv.delete(*tv.get_children())
            for i in db.fetch_ordem():
                tv.insert("", END, values=i)

        def insert():
            db.insertorc(cpfCliente_entry.get(), cpfMecanico_entry.get(), valor_entry.get(), descricaoDoServico_entry.get())
            messagebox.showinfo("Sucesso", "Orçamento cadastrado")
            clearAll()
            displayAll()

        def del_orcamento():
            db.remove_ordem(row[0])
            clearAll()
            displayAll()

        def clearAll():
            cpfCliente.set("")
            cpfMecanico.set("")
            valor.set("")
            descricaoDoServico.set("")

        # cores
        co1 = "#D3D3D3"
        co2 = "#000080"
        fonte = "new times roman"

        db = Database("ordem.db")
        # janela gerenciamento de funcionários
        janela = Toplevel()
        janela.title("Cadastro orçamento")
        janela.geometry("900x500")
        janela.resizable(width=False, height=False)

        cpfCliente = StringVar()
        cpfMecanico = StringVar()
        valor = StringVar()
        descricaoDoServico = StringVar()

        # criando frames
        frame_cima = Frame(janela, width=230, height=45, padx=1, bg=co2)
        frame_cima.grid(row=0, column=0, sticky=NSEW)

        frame_baixo = Frame(janela, width=230, height=400, padx=1)
        frame_baixo.grid(row=1, column=0, sticky=NSEW)

        frame_dir = Frame(janela, width=550, height=30, padx=1, bg=co1)
        frame_dir.grid(row=0, column=1, sticky=NSEW, rowspan=2)

        # titulo
        titulo = Label(frame_cima, text="Ordem de Serviço", font=(fonte, 12), bg=co2, fg="white")
        titulo.place(x=4, y=10)

        # 
        cpfCliente_label = Label(frame_baixo, text="CPF-Cliente: ")
        #cpfCliente_label.place(x=5, y=10)
        cpfCliente_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=cpfCliente)
        #cpfCliente_entry.place(x=8, y=30)

        # 
        cpfMecanico_label = Label(frame_baixo, text="CPF-Mecanico: ")
        #cpfMecanico_label.place(x=5, y=60)
        cpfMecanico_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=cpfMecanico)
        #cpfMecanico_entry.place(x=8, y=80)

        # 
        valor_label = Label(frame_baixo, text="Valor: ")
        #valor_label.place(x=5, y=110)
        valor_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=valor)
        #valor_entry.place(x=8, y=130)

        # 
        descricaoDoServico_label = Label(frame_baixo, text="Descricao Serviço: ")
        #descricaoDoServico_label.place(x=5, y=160)
        descricaoDoServico_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=descricaoDoServico)
        #descricaoDoServico_entry.place(x=8, y=180)

        # botão adicionar 
        add_btn = Button(frame_baixo, text="mkonj", command=insert, width=27)
        add_btn.place(x=8, y=18)

        # botão editar 
        edit_btn = Button(frame_baixo, text="Excluir", command=del_orcamento, width=27)
        edit_btn.place(x=8, y=50)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=("Calibri", 14), rowheight=47)
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 12))

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
        tv.column("4", width=50, stretch=NO)
        tv.heading("5", text="Descricao do Servico")
        tv.column("5", width=300, stretch=NO)
        tv["show"] = "headings"
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill=X)


        displayAll()

        mainloop()
