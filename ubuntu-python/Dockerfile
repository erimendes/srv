# Usar imagem base do Ubuntu
FROM ubuntu

# Atualizar pacotes e instalar o tzdata, Apache e dependências de sistema
RUN apt-get update && \
    apt-get install -y tzdata \
    apache2 gcc libffi-dev \
    python3-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Instalar as dependências do projeto
RUN pip3 install --no-cache-dir -r /opt/app/requirements.txt

# Expor a porta 80 para o servidor Apache
EXPOSE 80

# Comando para iniciar o Apache em foreground
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
