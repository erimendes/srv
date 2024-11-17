# Use a imagem base do Ubuntu
FROM ubuntu:latest

# Instale os pacotes necessários
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y tzdata apache2 gcc libffi-dev python3-dev build-essential python3-pip python3-venv mariadb-server && \
    rm -rf /var/lib/apt/lists/*

# Crie e ative um ambiente virtual Python
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Instale o mysql-connector-python usando pip3 no ambiente virtual
RUN pip3 install --no-cache-dir mysql-connector-python
#RUN apt install python3-mysqldb

RUN pip3 install flup
#RUN python3 -m pip install flup
# Configuração adicional (opcional)
# Exemplo: Exponha a porta 80 para o Apache
EXPOSE 80

# Comando para iniciar o servidor Apache
CMD ["apache2ctl", "-D", "FOREGROUND"]
