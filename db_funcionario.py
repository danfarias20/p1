import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, senha INTEGER,
         cpf TEXT, cargo TEXT)"""
        self.cursor.execute(sql)
        self.con.commit()

    def insert(self, nome, senha, cpf, cargo):
        self.cursor.execute("INSERT INTO funcionarios VALUES (NULL, ?, ?, ?, ?)", (nome, senha, cpf, cargo))
        self.con.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM funcionarios")
        linhas = self.cursor.fetchall()
        return linhas

    def remove(self, id):
        self.cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id, ))
        self.con.commit()

    def update(self, id, nome, senha, cpf, cargo):
        self.cursor.execute("UPDATE funcionarios SET nome=?, senha=?, cpf=?, cargo=? WHERE id=?", (nome, senha, cpf,
                                                                                                   cargo, id))
        self.con.commit()
