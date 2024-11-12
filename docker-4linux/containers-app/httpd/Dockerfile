# Usar uma imagem base do Apache
FROM httpd:latest

# Habilitar os módulos Apache necessários
RUN apt-get update && \
    apt-get install -y apache2-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expor a porta 80
EXPOSE 80

# Configurar o comando para iniciar o Apache em segundo plano
CMD ["httpd-foreground"]
