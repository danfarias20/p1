import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()

        sql1 = """CREATE TABLE IF NOT EXISTS orcamentos(id INTEGER PRIMARY KEY AUTOINCREMENT, cpf_cliente TEXT, 
                cpf_mecanico TEXT, valor TEXT, descricao_do_servico TEXT, status TEXT)"""
        sql2 = """CREATE TABLE IF NOT EXISTS ordem(id INTEGER PRIMARY KEY AUTOINCREMENT, cpf_cliente TEXT, 
                cpf_mecanico TEXT, valor TEXT, descricao_do_servico TEXT, status TEXT)"""

        self.cursor.execute(sql1)
        self.cursor.execute(sql2)

        self.con.commit()

    # ordem de serviço
    def concluir_ordem(self, id):
        self.cursor.execute("UPDATE ordem SET status=CONCLUÍDA WHERE id=?", id)
        self.con.commit()

    def fetch_ordem(self):
        self.cursor.execute("SELECT * FROM ordem")
        linhas = self.cursor.fetchall()
        return linhas

    def remove_ordem(self, id):
        self.cursor.execute("DELETE FROM ordem WHERE id = ?", (id,))
        self.con.commit()

    def mostrar_concluidas(self):
        self.cursor.execute("SELECT * FROM ordem WHERE status=CONCLUÍDAS")
        linhas = self.cursor.fetchall()
        return linhas

    def mostrar_ativas(self):
        self.cursor.execute("SELECT * FROM ordem WHERE status=ATIVAS")
        linhas = self.cursor.fetchall()
        return linhas

    # orçamentos
    def insertorc(self, cfp_cliente, cpf_mecanico, valor, descricao):
        self.cursor.execute("INSERT INTO orcamentos VALUES (NULL, ?, ?, ?, ?, NULL)", (cfp_cliente, cpf_mecanico, valor,
                                                                                       descricao))
        self.con.commit()

    def fetch_orcamento(self):
        self.cursor.execute("SELECT * FROM orcamentos")
        linhas = self.cursor.fetchall()
        return linhas

    def remove_orcamento(self, id):
        self.cursor.execute("DELETE FROM orcamentos WHERE id = ?", (id, ))
        self.con.commit()

    def updateorc(self, id, cfp_cliente, cpf_mecanico, valor, descricao):
        self.cursor.execute("UPDATE orcamentos SET cpf_cliente=?, cpf_mecanico=?, valor=?, descricao=?, "
                            "WHERE id=?", (cfp_cliente, cpf_mecanico, valor, descricao, id))
        self.con.commit()

    def trans_ordem(self, id):
        self.cursor.execute("INSERT INTO ordem SELECT * FROM orcamentos WHERE id=?", (id, ))
        self.con.commit()
        self.cursor.execute("DELETE FROM orcamentos WHERE id = ?", (id, ))
        self.cursor.execute("UPDATE ordem SET status=? WHERE id=?", ("ativa", id))

