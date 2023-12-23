# LINUX BASICOS:
### 1) Obtener los nombres de los ficheros de un listado ls -lh
~~~ 
ls -lh | rev | cut -d" " -f1 | rev ̣--> Usando cut y rev  
~~~
### 2) Obtener los 10 procesos que más RAM y CPU consumen
``ps aux | head -n10 | sort -nr -k 3 `` <strong>--> Los 10 procesos que más CPU consumen</strong>

``ps aux | head -n10 | sort -nr -k 4 `` <strong>--> Los 10 procesos que más CPU consumen</strong>

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

### 5) Vaciar archivos pesados con /dev/null

``cat /dev/null > ERR.log``  <strong> --> Vaciar él contenido del archivo ERR.log(Redirigiendo null)  y actualizar la fecha del fichero.</strong>

``> access.log`` <strong> --> Vaciar él contenido de access.log</strong>

``echo > access.log `` <strong> --> Vaciar él contenido de access.log</strong>

``cp /dev/null  access.log`` <strong> -->  Vaciar él contenido de access.log</strong>

``cat README.md 2> /dev/null `` <strong> --> Redirigir él STDERR al archivo dispositivo null.</strong>

### 5) Awk
