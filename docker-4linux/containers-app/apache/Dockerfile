# Use uma imagem base do Ubuntu
FROM ubuntu:20.04

# Defina as variáveis de ambiente para evitar interações durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualize e instale o Apache2 e o MariaDB
RUN apt-get update && \
    apt-get install -y apache2 mariadb-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure o Apache2 e MariaDB para não iniciar automaticamente durante o build
RUN service apache2 stop && \
    service mysql stop

# Exponha as portas
EXPOSE 80
EXPOSE 3306

# Inicie o Apache2 e o MariaDB diretamente no comando CMD
CMD service apache2 start && service mysql start && tail -f /dev/null
