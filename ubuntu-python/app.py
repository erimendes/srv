

import pymysql
from db import get_db, close_db
from faker import Faker
from flask import Flask, render_template

faker = Faker()

app = Flask(__name__)
app.teardown_appcontext(close_db)  # Chama close_db a cada fim de execução

@app.before_first_request
def initialize_db():
    """Cria a tabela 'usuarios' se ela não existir, antes do primeiro request."""
    con = get_db()
    cur = con.cursor(pymysql.cursors.DictCursor)
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INT AUTO_INCREMENT PRIMARY KEY, 
                        nome VARCHAR(255), 
                        email VARCHAR(255))''')
        con.commit()
    except pymysql.MySQLError as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        cur.close()

@app.route('/')
def home():
    """Exibe a lista de usuários e cria um novo usuário com dados fictícios."""
    con = get_db()
    cur = con.cursor(pymysql.cursors.DictCursor)
    try:
        # Insere um novo usuário fictício
        cur.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (faker.name(), faker.email()))
        con.commit()  # Não se esqueça de dar commit após a inserção
    except pymysql.MySQLError as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        cur.close()

    # Recupera todos os usuários da tabela
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM usuarios')
    usuarios = cur.fetchall()
    cur.close()
    
    return render_template('index.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
