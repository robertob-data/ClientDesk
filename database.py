import sqlite3


def conectar():
    conecao = sqlite3.connect('database.db')
    conecao.execute('PRAGMA foreign_keys = ON')
    return conecao

def criar_tabelas():
    conecao = conectar()
    cursor = conecao.cursor()

    cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL,
                    empresa TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    email TEXT,
                    servico TEXT NOT NULL,
                    valor_mensal REAL NOT NULL,
                    dia_vencimento INTEGER NOT NULL,
                    data_inicio TEXT NOT NULL,
                    status TEXT NOT NULL,
                    observacoes TEXT)''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS pagamentos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER REFERENCES clientes(id) NOT NULL,
                data_vencimento TEXT NOT NULL,
                data_pagamento TEXT,
                valor REAL NOT NULL,
                status TEXT NOT NULL)''')

    conecao.commit()
    conecao.close()

if __name__ == "__main__":
    criar_tabelas()