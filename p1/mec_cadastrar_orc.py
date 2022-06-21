from tkinter import ttk
from db_ordem_orcamentos import *
from tkinter import messagebox
from tkinter import *


class CadastroOrc:
    def __init__(self):
        def get_data(event):
            # pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
            selected_row = tv.focus()
            # pega o item(funcionário) que está nessa linha da tabela
            data = tv.item(selected_row)
            global row
            row = data["values"]
            cpf_cliente.set(row[1])
            cpf_mecanico.set(row[2])
            valor.set(row[3])
            descricao_entry.delete(1.0, END)
            descricao_entry.insert(END, row[4])

        def display_all():
            tv.delete(*tv.get_children())
            for i in db.fetch_orcamentos():
                tv.insert("", END, values=i)

        def insert():
            if cpf_cliente_entry.get() == "" or cpf_mecanico_entry.get() == "" or valor_entry.get() == ""\
                    or descricao_entry.get(1.0, END) == "":
                messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
            else:
                db.insertorc(cpf_cliente_entry.get(), cpf_mecanico_entry.get(), valor_entry.get(),
                             descricao_entry.get(1.0, END))
                clear_all()
                display_all()

        def update():
            if cpf_cliente_entry.get() == "" or cpf_mecanico_entry.get() == "" or valor_entry.get() == ""\
                    or descricao_entry.get(1.0, END) == "":
                messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
            else:
                db.updateorc(cpf_cliente_entry.get(), cpf_mecanico_entry.get(), valor_entry.get(),
                             descricao_entry.get(1.0, END))
                clear_all()
                display_all()

        def clear_all():
            cpf_cliente.set("")
            cpf_mecanico.set("")
            valor.set("")
            descricao_entry.delete(1.0, END)

        # cores
        co1 = "#D3D3D3"
        co2 = "#000080"
        fonte = "new times roman"

        db = Database("orcamentos.db")

        janela = Toplevel()
        janela.title("Cadastro orçamento")
        janela.geometry("900x500")
        janela.resizable(width=False, height=False)

        cpf_cliente = StringVar()
        cpf_mecanico = StringVar()
        valor = StringVar()
        descricao = StringVar()

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

        # 
        cpf_cliente_label = Label(frame_baixo, text="CPF-Cliente: ")
        cpf_cliente_label.place(x=5, y=10)
        cpf_cliente_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=cpf_cliente)
        cpf_cliente_entry.place(x=8, y=30)

        # 
        cpf_mecanico_label = Label(frame_baixo, text="CPF-Mecanico: ")
        cpf_mecanico_label.place(x=5, y=60)
        cpf_mecanico_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=cpf_mecanico)
        cpf_mecanico_entry.place(x=8, y=80)

        # 
        valor_label = Label(frame_baixo, text="Valor: ")
        valor_label.place(x=5, y=110)
        valor_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=valor)
        valor_entry.place(x=8, y=130)

        # 
        descricao_label = Label(frame_baixo, text="Descricao Serviço: ")
        descricao_label.place(x=5, y=160)
        descricao_entry = Text(frame_baixo, width=26, relief=SOLID, height=5)
        descricao_entry.place(x=8, y=180)

        # botão adicionar 
        add_btn = Button(frame_baixo, text="Cadastrar", command=insert, width=15)
        add_btn.place(x=8, y=280)

        # botão editar 
        edit_btn = Button(frame_baixo, text="Editar", command=update, width=15)
        edit_btn.place(x=8, y=320)

        # botão limpar
        limpar_btn = Button(frame_baixo, text="Limpar", command=clear_all, width=15)
        limpar_btn.place(x=8, y=360)

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

