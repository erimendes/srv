# #!/usr/bin/python3

# import pymysql

# from os import environ as env
# from flask import g

# def get_db():
#     '''Obtém a conexão com o banco.

#     g é uma variável global do Flask.
#     Caso nenhuma conexão tenha sido criada até então, uma nova
#     conexão é criada, guardada em g.db e retornada.
#     Chamadas subsequentes da mesma requisição utilizarão a conexão 
#     criada anteriormente dentro de g.db.'''
#     if 'db' not in g:
#         g.db = pymysql.connect(
#             host       = env['DB_HOST'],
#             db         = env['DB_NAME'],
#             user       = env['DB_USER'],
#             passwd     = env['DB_PASS'],
#             autocommit = True
#         )
#     return g.db

# def close_db(exception=None):
#     '''Remove db da variável g e fecha a conexão'''
#     db = g.pop('db', None)
#     if db:
#         db.close()

#!/usr/bin/python3

import pymysql
from os import environ as env
from flask import g, Flask

# Função para obter a conexão com o banco de dados
def get_db():
    '''Obtém a conexão com o banco.'''
    if 'db' not in g:
        try:
            # Verificar se todas as variáveis de ambiente necessárias estão presentes
            required_env_vars = ['DB_HOST', 'DB_NAME', 'DB_USER', 'DB_PASS']
            for var in required_env_vars:
                if var not in env:
                    raise EnvironmentError(f"Variável de ambiente {var} não encontrada!")

            g.db = pymysql.connect(
                host=env['DB_HOST'],
                db=env['DB_NAME'],
                user=env['DB_USER'],
                password=env['DB_PASS'],
                autocommit=True
            )
        except pymysql.MySQLError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise  # Re-levanta a exceção
    return g.db

# Função para fechar a conexão com o banco de dados
def close_db(exception=None):
    '''Remove db da variável g e fecha a conexão'''
    db = g.pop('db', None)
    if db:
        db.close()

# Configuração do Flask
app = Flask(__name__)

# Registra a função de fechamento de DB
app.teardown_appcontext(close_db)

# Exemplo de rota
@app.route('/')
def index():
    db = get_db()  # Obtém a conexão com o banco
    return "Conexão com o banco de dados bem-sucedida!"

if __name__ == '__main__':
    app.run(debug=True)
