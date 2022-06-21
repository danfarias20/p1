from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tela_gerente import *
from db_funcionario import *


class GerenteFunc:
    def __init__(self):
        def getData(event):
            # pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
            selected_row = tv.focus()
            # pega o item(funcionário) que está nessa linha da tabela
            data = tv.item(selected_row)
            global row
            row = data["values"]
            nome.set(row[1])
            senha.set(row[2])
            cpf.set(row[3])
            cargo.set(row[4])

        def displayAll():
            tv.delete(*tv.get_children())
            for i in db.fetch():
                tv.insert("", END, values=i)

        def add_funcionario():
            if nome_entry.get() == "" or senha_entry.get() == "" or cpf_entry.get() == ""\
                    or cargo_entry.get() == "":
                messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
            else:
                db.insert(nome_entry.get(), senha_entry.get(), cpf_entry.get(), cargo_entry.get())
                clear_all()
                displayAll()

        def edit_funcionario():
            if nome_entry.get() == "" or senha_entry.get() == "" or cpf_entry.get() == ""\
                    or cargo_entry.get() == "":
                messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
            else:
                db.update(row[0], nome_entry.get(), senha_entry.get(), cpf_entry.get(), cargo_entry.get())
                clear_all()
                displayAll()

        def del_funcionario():
            db.remove(row[0])
            clear_all()
            displayAll()

        def clear_all():
            nome.set("")
            senha.set("")
            cpf.set("")
            cargo.set("")

        # cores
        co1 = "#D3D3D3"
        co2 = "#000080"
        fonte = "new times roman"

        db = Database("funcionarios.db")

        # janela gerenciamento de funcionários
        janela = Toplevel()
        janela.title("Gerenciamento de funcionários")
        janela.geometry("900x500")
        janela.resizable(width=False, height=False)

        nome = StringVar()
        senha = StringVar()
        cpf = StringVar()
        cargo = StringVar()

        # criando frames
        frame_cima = Frame(janela, width=230, height=45, padx=1, bg=co2)
        frame_cima.grid(row=0, column=0, sticky=NSEW)

        frame_baixo = Frame(janela, width=230, height=400, padx=1)
        frame_baixo.grid(row=1, column=0, sticky=NSEW)

        frame_dir = Frame(janela, width=550, height=40, padx=1, bg=co1)
        frame_dir.grid(row=0, column=1, sticky=NSEW, rowspan=2)

        # titulo
        titulo = Label(frame_cima, text="Gerenciamento de funcionários", font=(fonte, 12), bg=co2, fg="white")
        titulo.place(x=4, y=10)

        # nome do funcionário
        nome_label = Label(frame_baixo, text="Nome: ")
        nome_label.place(x=5, y=10)
        nome_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=nome)
        nome_entry.place(x=8, y=30)

        # senha do funcionário
        senha_label = Label(frame_baixo, text="Senha: ")
        senha_label.place(x=5, y=60)
        senha_entry = Entry(frame_baixo, width=35, relief=SOLID, show="*", textvariable=senha)
        senha_entry.place(x=8, y=80)

        # cpf do funcionário
        cpf_label = Label(frame_baixo, text="CPF: ")
        cpf_label.place(x=5, y=110)
        cpf_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=cpf)
        cpf_entry.place(x=8, y=130)

        # cargo do funcionário
        cargo_label = Label(frame_baixo, text="Cargo: ")
        cargo_label.place(x=5, y=160)
        cargo_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=cargo)
        cargo_entry.place(x=8, y=180)

        # botão adicionar funcionário
        add_btn = Button(frame_baixo, text="Adicionar", command=add_funcionario, width=15)
        add_btn.place(x=8, y=220)

        # botão editar funcionário
        edit_btn = Button(frame_baixo, text="Editar", command=edit_funcionario, width=15)
        edit_btn.place(x=8, y=260)

        # botão deletar funcionário
        delete_btn = Button(frame_baixo, text="deletar", command=del_funcionario, width=15)
        delete_btn.place(x=8, y=300)

        # botão limpar
        limpar_btn = Button(frame_baixo, text="Limpar", command=clear_all, width=15)
        limpar_btn.place(x=8, y=340)

        style = ttk.Style()
        style.configure("mystyle.Treeview", rowheight=30)
        style.configure("mystyle.Treeview.Heading")

        sb = Scrollbar(frame_dir)

        sb.pack(fill=Y, side=RIGHT)
        # Criando a tabela de fato
        tv = ttk.Treeview(frame_dir, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")
        tv.heading("1", text="ID")
        tv.column("1", width=30, stretch=NO)
        tv.heading("2", text="Nome")
        tv.column("2", width=200, stretch=NO)
        tv.heading("3", text="Senha")
        tv.column("3", width=120, stretch=NO)
        tv.heading("4", text="CPF")
        tv.column("4", width=150, stretch=NO)
        tv.heading("5", text="Cargo")
        tv.column("5", width=150, stretch=NO)
        tv["show"] = "headings"
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill=X)

        displayAll()

        mainloop()
