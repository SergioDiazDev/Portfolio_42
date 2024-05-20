#!/bin/bash

# Comando para iniciar tu aplicación
python3 /root/Desktop/Portfolio.py &

# Esperar a que haya conexiones entrantes en el puerto 4242 (localhost)
while ! nc -z localhost 4242; do
    sleep 1
done

# Mantener el contenedor en ejecución
tail -f /dev/null
