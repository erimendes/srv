FROM python:3.9-alpine

# Expor a porta 5000 para o Flask
EXPOSE 5000

# Instalar dependências do sistema (para compilação de pacotes Python)
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev \
    py3-pip

# Copiar os arquivos para dentro do contêiner
COPY . /opt/app

# Instalar as dependências do projeto
RUN pip3 install --no-cache-dir -r /opt/app/requirements.txt

# Definir o diretório de trabalho
WORKDIR /opt/app

# Definir a variável de ambiente FLASK_APP para o Flask
ENV FLASK_APP=app.py

# Rodar o Flask com o host em 0.0.0.0 para escutar todas as interfaces
CMD ["flask", "run", "--host", "0.0.0.0"]
