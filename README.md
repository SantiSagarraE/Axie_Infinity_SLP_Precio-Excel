# Axie_Infinity_SLP_Precio-Excel
Programa enfocado a jugadores de Axie infinity para llevar a cabo una base de datos en excel sobre el SLP y su precio diariamente.

Para su correcto funcionamiento se debe tener instalado:

-->Python y los paquetes Scrapy y Openpyxl

Como correr el programa:

Dentro del directorio del proyecto ejecutar en la terminal:


-->Scrapy crawl SLPdata -o SLPdata.csv 


Lo que hace es guardar el precio del SLP en un archivo de texto llamado SLPdata.csv


Luego correr el programa 'SLPexcel.py' lo que genera el archivo excel con el precio del SLP.
