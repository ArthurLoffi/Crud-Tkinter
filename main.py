from tkinter import *
from tkinter import ttk
import db

# Conexão com o banco de dados
conn = db.conectar()
cursor = conn.cursor()

# Iniciando o tk
app = Tk()
app.title("Cadastro de Usuários")
frm = ttk.Frame(app, padding=50)

# Definindo a cor de fundo
ttk.Style().configure(app, background="grey")
frm.grid()
style = ttk.Style()

# Definindo a cor do label
style.configure("BW.TLabel", foreground="black")
style.configure("Sucesso.TLabel", foreground="green", background="white")
# Criando um label
ttk.Label(frm, text="Salvar usuário", style="BW.TLabel").grid(column=0, row=0)

# Criando um input
email = ttk.Entry(frm, width=30)
email.grid(column=0, row=1)
# Deixa ele selecionado quando inicia o programa
email.focus()

# Função para receber os dados
def receberDados():
    valor = email.get()
    sql = f'INSERT INTO usuarios (email) VALUES ("{valor}")'
    cursor.execute(sql)
    conn.commit()
    #Mostrar mensagem de sucesso
    ttk.Label(frm, text="Sucesso ao cadastrar usuário", style="Sucesso.TLabel").grid(column=0, row=3)

# Botão para iniciar a função
ttk.Button(frm, text="Enviar",command=receberDados).grid(column=0, row=2)

def ao_fechar():
    db.fechar_conexao(conn, cursor)
    app.destroy()

#Protocolo para fechar a conexão ao fechar a aba
app.protocol("WM_DELETE_WINDOW", ao_fechar)
app.mainloop()