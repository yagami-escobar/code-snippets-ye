# LINUX BASICOS:
### 1) Obtener los nombres de los ficheros de un listado ls -lh
``ls -lh | rev | cut -d" " -f1 | rev`` ̣_--> Usando cut y rev_

### 2) Obtener los 10 procesos que más RAM y CPU consumen
``ps aux | head -n10 | sort -nr -k 3 `` _--> Los 10 procesos que más CPU consumen_

``ps aux | head -n10 | sort -nr -k 4 `` _--> Los 10 procesos que más CPU consumen_

### 3) Dividir un archivo de 1K Lineas en 10 archivos con 100 lines.
`` split -l 100 file.txt jyp``

### 4) Escribir varias lineas en un VAR ENV o FILE, etc

_Permite asignar Imperativamente cadenas de texto de varias Lineas a una Variable de Shell, archivo, etc_

~~~
sql = $(cat << EOF
SELECT p.name, p.precio, p.detalle 
FROM productos p
WHERE p.name = 'laptop_hp'
EOF
~~~

### 5) Vaciar archivos pesados con /dev/null

``cat /dev/null > ERR.log``  _--> Vaciar él contenido del archivo ERR.log(Redirigiendo null)  y actualizar la fecha del fichero_

``> access.log`` _--> Vaciar él contenido de access.log_

``echo > access.log `` _--> Vaciar él contenido de access.log_

``cp /dev/null  access.log`` _-->  Vaciar él contenido de access.log_

``cat README.md 2> /dev/null `` _--> Redirigir él STDERR al archivo dispositivo null._

### 6) Awk
_## Imprime los 4 primeros valores tomando cómo patrón de filtro los 2 puntos(:) e imprime una flecha y luego imprime toda la línea_

``cat /etc/passwd | head -n5 | awk -F: ‘{print $1,$2,$3,$4,”---->”,$0}’
``

``awk -F: ‘{print  $1}’ /etc/passwd  || cut -d: -f1 /etc/passwd`` _--> Elegir qué campo mostrar._

_## Imprime los 4 primeros valores tomando cómo patrón de filtro él guión(-) e imprime una flecha y luego imprime toda la línea_

``cat users5.log | awk -F- ‘{print $1,$2,$3,$4,”---->”,$0}’``

_## Imprime él Número de línea de visualización (NR), luego 2 valores y luego él último campo($NF)_

``cat users5.log | awk -F- ‘{print NR,$1,$2,$NF}’``

### 7) Imprimir la lista de Sistema de Ficheros que está más consumido
``df -h | head -n1 && df -h | tail -n+2 | sort -nr -k 5``

- _Primera parte solo me imprime la cabecera_

- _Segunda parte me imprime todo lo qué está de la cabecera para abajo ordenando de mayor a menor comenzando por la 5ta columna_

``df -h | head -n1 && df -h | sed  1d| sort -nr -k 5``
- _Hace lo mismo qué él anterior solo reemplazamos él tail por él sed, él sed suprime la primera línea._

### 8) Curls
``curl -LO http://google.apis./resource.tar.gz``

``curl -s http://10.244.2.3:8888 | jq “”.HOSTNAME``

``curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee jenkins1.asc > /dev/nul`` _--> Duplica la salida traida por él curl y lo guarda en él archivo del tee y omite la última salida._

### 9) Find
``find ./ -type d -iname “network-script”`` _--> Buscar él directorio qué contenga en su nombre network-script_

### 10) Jq
``kubectl -n yapp get secret/password | jq ‘.metadata.name, type, .[]’`` _--> Devuelve el valor del campo nombre, type y todos los valores del 1er nivel del JSON_

### 11) Cp
``cp -rv  .  ~/repo-cursos/curso-terraform`` _--> Copiar tanto archivos y directorios de una ruta a otra_

### 12) Grep
``git log | grep -i author | sort | uniq |nl`` _--> Busca las líneas qué contengan author, ordena y elimina duplicadas y enumera lineas._

``kubectl -n ntlc get pods | grep -e api-v1 -e ai-v2 -e api-v3 `` _--> Lista diferentes tipos de pods con grep_

<br />

# SHELL BASICOS

### 1) Ejecutar Loop en Linux

**Loop Varias Líneas:**
~~~
sh -c ‘while true; \
do \
echo “Hello World”; \
sleep 1; \
done’ 
~~~

**Loop 1 Línea:**
~~~
for i in $(seq 10); do echo “Hello World”;done
~~~

### 2) Ejecutar X Curls:
~~~
sh -c ‘for i in $(seq 10); \
do \
curl localhost:8080/ready; \
echo “Le pegue $i”; \
done’

sh -c 'i=1; while [ $i -le 11 ]; do curl localhost:8080/ready $((i++)); done'
~~~

### 3) Correr sh:
`` /bin/sh -xe /tmp/jenkins2315316312.sh ``

`` sh -xec 'echo “DONE”’ `` _--> Imprime la salida cómo proceso + Salida limpia._

`` sh -c ‘echo “DONE”’ `` _--> Imprime la salida limpia._

### 4) Sequencias:
`` seq 1 10 `` _--> Imprime del 1 al 10_

### 5) Eliminar Interfacez veth VMs:
~~~
veth_list=$(ifconfig | grep “veth” | cut -d“:” -f1)
for i in $veth_list; do sudo ip link set $veth_list down; done
for i in $veth_list; do sudo ip link delete $veth_list; done
~~~
<br />

# DOCKER
### 1) Eliminar Containers
~~~
#! /bin/bash
for i in $(seq 4);
do
 docker rm jenkins-c$i;
done
~~~