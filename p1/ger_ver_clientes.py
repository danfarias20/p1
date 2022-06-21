from tkinter import *
from tela_gerente import *
from tkinter import ttk
from db_clientes import *

# cores
co1 = "#D3D3D3"
co2 = "#000080"


class VerClientes:
    def __init__(self):
        def getData(event):
            # pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
            selected_row = tv.focus()

            data = tv.item(selected_row)
            global row
            row = data["values"]
            nome.set(row[1])
            cpf.set(row[2])
            email.set(row[3])
            telefone.set(row[4])
            placa.set(row[5])
            endereco_entry.delete(1.0, END)
            endereco_entry.insert(END, row[6])

        def displayAll():
            tv.delete(*tv.get_children())
            for i in db.fetch():
                tv.insert("", END, values=i)
        
        def del_cliente():
            db.remove(row[0])
            clearAll()
            displayAll()

        def clearAll():
            nome.set("")
            cpf.set("")
            email.set("")
            telefone.set("")
            placa.set("")
            endereco_entry.delete(1.0, END)

        # cores
        co1 = "#D3D3D3"
        co2 = "#000080"
        fonte = "new times roman"

        db = Database("clientes.db")

        # janela gerenciamento de funcionários
        janela = Toplevel()
        janela.title("Clientes")
        janela.geometry("1000x500")
        janela.resizable(width=False, height=False)

        nome = StringVar()
        cpf = StringVar()
        email = StringVar()
        telefone = StringVar()
        placa = StringVar()

        # criando frames
        frame_cima = Frame(janela, width=230, height=45, padx=1, bg=co2)
        frame_cima.grid(row=0, column=0, sticky=NSEW)

        frame_baixo = Frame(janela, width=230, height=400, padx=1)
        frame_baixo.grid(row=1, column=0, sticky=NSEW)

        frame_dir = Frame(janela, width=650, height=30, padx=1, bg=co1)
        frame_dir.grid(row=0, column=1, sticky=NSEW, rowspan=2)

        # titulo
        titulo = Label(frame_cima, text="Clientes", font=(fonte, 12), bg=co2, fg="white")
        titulo.place(x=76, y=10)

        # # nome do cliente
        # nome_label = Label(frame_baixo, text="Nome: ")
        # nome_label.place(x=5, y=10)
        # nome_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=nome)
        # nome_entry.place(x=8, y=30)

        # # cpf do cliente
        # cpf_label = Label(frame_baixo, text="Cpf: ")
        # cpf_label.place(x=5, y=60)
        # cpf_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=cpf)
        # cpf_entry.place(x=8, y=80)

        # # email do cliente
        # email_label = Label(frame_baixo, text="Email: ")
        # email_label.place(x=5, y=110)
        # email_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=email)
        # email_entry.place(x=8, y=130)

        # # telefone do cliente
        # telefone_label = Label(frame_baixo, text="Telefone: ")
        # telefone_label.place(x=5, y=160)
        # telefone_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=telefone)
        # telefone_entry.place(x=8, y=180)

        # # placa do carro do cliente
        # placa_label = Label(frame_baixo, text="Placa o carro: ")
        # placa_label.place(x=5, y=210)
        # placa_entry = Entry(frame_baixo, width=35, relief=SOLID, textvariable=placa)
        # placa_entry.place(x=8, y=230)

        # # cargo do cliente
        # endereco_label = Label(frame_baixo, text="Endereço: ")
        # endereco_label.place(x=5, y=260)
        endereco_entry = Text(frame_baixo, width=26, relief=SOLID, height=5)

        # botão adicionar cliente
        add_btn = Button(frame_baixo, text="Excluir", command=del_cliente, width=27)
        add_btn.place(x=8, y=16)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=("Calibri", 14), rowheight=47)
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 12))

        sb = Scrollbar(frame_dir)

        sb.pack(fill=Y, side=RIGHT)
        # Criando a tabela de fato
        tv = ttk.Treeview(frame_dir, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
        tv.heading("1", text="ID")
        tv.column("1", width=25, stretch=NO)
        tv.heading("2", text="Nome")
        tv.column("2", width=155, stretch=NO)
        tv.heading("3", text="CPF")
        tv.column("3", width=90, stretch=NO)
        tv.heading("4", text="Email")
        tv.column("4", width=120, stretch=NO)
        tv.heading("5", text="Telefone")
        tv.column("5", width=120, stretch=NO)
        tv.heading("6", text="Placa do carro")
        tv.column("6", width=120, stretch=NO)
        tv.heading("7", text="Endereço")
        tv.column("7", width=120, stretch=NO)
        tv["show"] = "headings"
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill=X)

        displayAll()

        mainloop()