import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()

        sql = """CREATE TABLE IF NOT EXISTS orcamentos(id INTEGER PRIMARY KEY AUTOINCREMENT, cpf_cliente TEXT, 
                cpf_mecanico TEXT, valor TEXT, descricao_do_servico TEXT, status TEXT)"""

        self.cursor.execute(sql)

        self.con.commit()

    def fetch_orcamentos(self):
        self.cursor.execute("SELECT * FROM orcamentos WHERE status = 'orçamento'")
        linhas = self.cursor.fetchall()
        return linhas

    def remove_orcamento(self, id):
        self.cursor.execute("DELETE FROM orcamentos WHERE id = ?", (id,))
        self.con.commit()

    def trans_ordem(self, id):
        self.cursor.execute("UPDATE orcamentos SET status = 'ativa' WHERE id = ?", (id, ))
        self.con.commit()

    def fetch_ordem(self):
        self.cursor.execute("SELECT * FROM orcamentos WHERE status = 'ativa'")
        self.cursor.execute("SELECT * FROM orcamentos WHERE status = 'concluída'")
        linhas = self.cursor.fetchall()
        return linhas

    def fetch_ordem_mec(self, cpf_mecanico):
        self.cursor.execute("SELECT * FROM orcamentos WHERE status = 'ativa' and cpf_mecanico = ?", cpf_mecanico)
        linhas = self.cursor.fetchall()
        return linhas

    def insertorc(self, cpf_cliente, cpf_mecanico, valor, descricao):
        self.cursor.execute("INSERT INTO orcamentos VALUES (NULL, ?, ?, ?, ?, 'orçamento')", (cpf_cliente, cpf_mecanico, valor,
                                                                                       descricao))
        self.con.commit()

    def updateorc(self, id, cpf_cliente, cpf_mecanico, valor, descricao):
        self.cursor.execute("UPDATE orcamentos SET cpf_cliente=?, cpf_mecanico=?, valor=?, descricao_do_servico=?, "
                            "WHERE id=?", (cpf_cliente, cpf_mecanico, valor, descricao, id))
        self.con.commit()

    def concluir_ordem(self, id):
        self.cursor.execute("UPDATE orcamentos SET status='concluída' WHERE id=?", (id, ))
        self.con.commit()
