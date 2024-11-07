# Containers - Aplicações

Neste repositório existem os mais diversos exemplos de diferentes aplicações utilizando diferentes linguagens de programação e arquiteturas para o curso gratuito de contêineres da 4Linux.

Construir imagem:
docker image build --tag flask

docker container run --detach -e DB_HOST=172.18.0.2 -e DB_USER=container -e DB_PASS=4linux -e DB_NAME=container -p 5000:5000 --name flask flask

docker logs -f flask

https://labs.play-with-docker.com/