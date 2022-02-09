# Axie_Infinity_SLP_Precio-Excel
Programa enfocado a jugadores de Axie infinity para llevar a cabo una base de datos en excel sobre el SLP y su precio diariamente.

Para su correcto funcionamiento se debe tener instalado:

-->Python y los paquetes Scrapy y Openpyxl

Como correr el programa:

Primero debemos crear un proyecto Scrapy:

Dentro de una terminal (cmd en Windows) nos dirigimos hacia donde queremos guardar el proyecto y ejecutamos lo siguiente:

-->Scrapy startproject SLP_data

Dentro de la carpeta del proyecto pegamos el programa:

-->SLPexcel.py

Luego, entramos a la carpeta SLP_data y pegamos/reemplazamos los programas:

--> settings.py y exporters.py

Luego nos dirigimos a la carpeta 'Spiders' dentro del proyecto creado y pegamos el programa:

-->SLP.py

A continuacion, abrimos una terminal, nos dirigimos al directorio del proyecto y ejecutamos:

-->Scrapy crawl SLPdata -o SLPdata.csv 

Lo que hace es guardar el precio del SLP en un archivo de texto llamado SLPdata.csv

Finalmente correr el programa 'SLPexcel.py' lo que genera el archivo excel con el precio del SLP.
