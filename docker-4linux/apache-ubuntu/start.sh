#!/bin/bash

# Iniciar o serviço do MariaDB
service mysql start

# Iniciar o serviço do Apache
service apache2 start

# Manter o processo em execução para o container não ser fechado
tail -f /dev/null
