Criar imagem:
docker build -t python-apache . 

Criar container:
docker run -p 8080:80 python-apache

Para ver:
http://127.0.0.1:8080/

Alterar rota No Linux:
sudo nano /etc/hosts
127.0.0.1    meusite.com
mudar o wsgi.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

Alterar rota No windows:
C:\Windows\System32\drivers\etc\hosts
127.0.0.1    meusite.com
mudar o wsgi.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



http://130.1.0.247:81/oper/painel