# LINUX BASICOS:
### 1) Obtener los nombres de los ficheros de un listado ls -lh
~~~ 
ls -lh | rev | cut -d" " -f1 | rev ̣--> Usando cut y rev  
~~~
### 2) Obtener los 10 procesos que más RAM y CPU consumen
``ps aux | head -n10 | sort -nr -k 3 --> Los 10 procesos que más CPU consumen``

``ps aux | head -n10 | sort -nr -k 4 --> Los 10 procesos que más RAM consumen``

### 3) Dividir un archivo de 1K Lineas en 10 archivos con 100 lines.
`` split -l 100 file.txt jyp``

### 4) Escribir varias lineas en un VAR ENV o FILE, etc

<strong> Permite asignar Imperativamente cadenas de texto de varias Lineas a una Variable de Shell, archivo, etc</strong>

~~~
sql = $(cat << EOF
SELECT p.name, p.precio, p.detalle 
FROM productos p
WHERE p.name = 'laptop_hp'
EOF
~~~
 

