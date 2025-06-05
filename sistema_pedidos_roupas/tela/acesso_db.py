import sqlite3
from database.conexao import conectar

def inserir_pedido(cliente, produto, tamanho, quantidade, preco_unitario, data_pedido):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pedidos (cliente, produto, tamanho, quantidade, preco_unitario, data_pedido)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (cliente, produto, tamanho, quantidade, preco_unitario, data_pedido))

    conn.commit()
    conn.close()

def listar_pedidos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos