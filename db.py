# conexao_db.py
import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='crud_python',
    )


def fechar_conexao(conn, cursor):
    conn.close()
    cursor.close()