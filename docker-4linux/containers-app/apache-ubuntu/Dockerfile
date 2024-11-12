# Usar a imagem base do Ubuntu 24.04
FROM ubuntu:24.04

# Definir variáveis para evitar interatividade durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualizar pacotes e instalar Apache
RUN apt-get update && \
    apt-get install -y \
    apache2 \
    && rm -rf /var/lib/apt/lists/*

# Copiar o conteúdo da aplicação (exemplo: index.html) para o Apache
COPY gci /var/www/html

# Habilitar módulos Apache necessários
RUN a2enmod rewrite

# Expor a porta 80 para o Apache
EXPOSE 80

# Copiar a configuração personalizada do Apache
COPY gci.conf /etc/apache2/sites-available/000-default.conf

# Definir o comando de inicialização do container
CMD ["apache2ctl", "-D", "FOREGROUND"]
