import sqlite3


class Database:
    def __init__(self, db):
        # Cria a conexão com o banco
        self.con = sqlite3.connect(db)
        # Cria o cursor para as operações no banco
        self.cursor = self.con.cursor()
        # Comando para criar a tabela de funcionários
        sql = """CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf INTEGER,
         email TEXT, telefone TEXT, placa TEXT, endereco TEXT)"""
        # Executando o comando acima
        self.cursor.execute(sql)
        # Persistindo o que foi feito
        self.con.commit()

    def insert(self, nome, cpf, email, telefone, placa, endereco):
        self.cursor.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?, ?, ?)", (nome, cpf, email, telefone,
                                                                                     placa, endereco))
        self.con.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM clientes")
        linhas = self.cursor.fetchall()
        return linhas

    def remove(self, id):
        self.cursor.execute("DELETE FROM clientes WHERE id = ?", (id, ))
        self.con.commit()

    def update(self, id, nome, cpf, email, telefone, placa, endereco):
        self.cursor.execute("UPDATE clientes SET nome=?, cpf=?, email=?, telefone=?, placa=?, endereco=?, WHERE id=?",
                            (nome, cpf, email, telefone, placa, endereco, id))
        self.con.commit()
