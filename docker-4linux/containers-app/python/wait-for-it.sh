#!/bin/bash
# Wait for the MariaDB to be ready
until nc -z mariadb 3306; do
  echo "Waiting for MariaDB..."
  sleep 2
done

# Run the application
exec "$@"
