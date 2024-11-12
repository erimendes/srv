# Usar uma imagem base do Apache
FROM httpd:latest

WORKDIR /usr/local/apache2/htdocs/

COPY index.html /usr/local/apache2/htdocs/

# Expor a porta 80
EXPOSE 80

# Configurar o comando para iniciar o Apache em segundo plano
CMD ["httpd-foreground"]
