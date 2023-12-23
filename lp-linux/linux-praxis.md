# LINUX BASICOS:
### 1) Obtener los nombres de los ficheros de un listado ls -lh
~~~ 
ls -lh | rev | cut -d" " -f1 | rev ̣--> Usando cut y rev  
~~~
### 2) Obtener los 10 procesos que más RAM y CPU consumen
``ps aux | head -n10 | sort -nr -k 3 --> Los 10 procesos que más CPU consumen``

``ps aux | head -n10 | sort -nr -k 4 --> Los 10 procesos que más RAM consumen``


 

