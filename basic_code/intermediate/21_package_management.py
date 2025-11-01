"""_summary_

Manejo de paquetes en Python, usamos un gestor de paquetes en Python, 
esto en caso de que no contemos con algún modulo que necesitemos y 
queramos hacerlo de forma fácil y sencilla! Esto gracias a la herramienta:
PIP (Python Package Index).
También, pip nos ayuda hasta controlar la versión de python que usaremos
en nuestro proyecto.

En la lección veremos como: descargar dependencias a través de pip, cómo
usarlas dentro de nuestro proyecto o hasta crear nuestra propia 
dependencia. 

La instalación de pip lo podemos hacer a través de la terminal, puede
ser la que vemos dentro de nuestro IDE o en la de nuestro sistema.
Podemos comprobar primero si no lo tenemos instalado a través del comando:

    pip --version

En mi caso, ya lo tengo instalado en su versión 22.0.2, pero si hay que 
instalarlo usamos el comando: pip install pip. En caso de querer
actualizarlo usamos:

    pip install --upgrade pip

De preferencia, hay que hacer un entorno virtual para que no haya problemas
con las dependencias!
De aquí, ya solo es cuestión de agregar las dependencias que necesitemos 
instalar para nuestro proyecto.

---> Algunas librerías populares dentro de Python:
    - numpy: es muy útil y usada en ciencias computacionales en python, ya
             que permite trabajar de forma sencilla con arrays y matrices
             multidimensionales que pueden ser operadas con operaciones 
             matemáticas de alto nivel.
    
    - pandas: usada comunmente para trabajar con datos, es decir, archivos
              que contengan una gran cantidad de datos como hojas de excel.
              
    - requests: para realizar peticiones en web (esto se verá más adelante
                con otro proyecto)
    
Como nota adicional, podemos sacar un listado de las librerías que podemos 
cargar de forma predeterminada con pip (comando: pip list).
También así como podemos instalar, podemos desinstalar paquetes con el 
comando: uninstall.

Si queremos obtener información de un paquete instalado ponemos:

    pip show <nombre_paquete>


---> Creando nuestra propia librería / dependencia para subirla a pip:
    - Creamos una carpeta para almacenar.
    - Creamos un nuevo fichero llamado __init__.py para apuntarle al 
      sistema que queremos que todo eso se tome como una dependencia
      (esto lo estaré haciendo dentro de la carpeta de este proyecto).
      Este paso es muy importante para que se tome como un paquete para
      usar FUERA DEL PROYECTO. 
        * Dentro del paquete creamos la funcionalidad del paquete.
    - Hacemos los ficheros que contengan las operaciones que serán de
      la librería.
    - Importamos en nuestro programa el paquete que hemos creado.
    - Usamos los modulos sin problema

Nota: creo que por lo pronto no haré algo de instalación de estos paquetes.
"""

#### --> Llamando a paquete que hemos hecho
from my_package import artihmetics as a

print(f"Usando paquete creado por mi: {a.sum_two_numbers(10,20)}")