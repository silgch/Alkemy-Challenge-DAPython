# Challenge Data Analytics - Python (Alkemy)


## Objetivo 馃憟
Para resolver este challenge, se  cre贸 un proyecto que consume datos desde 3 fuentes distintas para popular una base de datos SQL con informaci贸n cultural sobre bibliotecas, museos y salas de cines argentinos.

## Herramientas Utilizadas 馃憟
Este proyecto se realizo en **Python** y se utilizaron las siguientes herramientas y bibliotecas para su desarrollo:
<ul>
<li>Los archivos fuentes se obtuvieron a trav茅s de la biblioteca <b>Request</b> </li>
<li>Para facilitar el deploy se creo un <b> entorno virtual venv .</b> </li>
<li>Para facilitar la conexi贸n a la base de datos y las configuraciones de las URL necesarias para descargar los archivos fuentes se utiliz贸 <b> Python-decouple.</b> </li>
<li>El procesamiento de datos se realiz贸 con la herramienta <b>Pandas. </b> </li>
<li>La conexi贸n a la Base de Datos se realiz贸 con la biblioteca <b>SQLalchemy </b> </li>
<li>La Base de datos utilizada es  <b>PostgreSQL </b> </li>
<li>El programa crea logs sobre su ejecuci贸n utilizando la library <b>Logging</b> </li>
</ul>

## Instrucciones de instalaci贸n 馃憟

1) CLONAR  EL PROYECTO <br>
*Se asume que se encuentra <b>git </b>instalado en la PC donde se quiere descargar el proyecto* <br>
En la PC donde  se quiere ejecutarse el proyecto, abrir una consola/terminal y desplazarse hasta la carpeta en donde se quiere instalar el mismo. Luego ejecutar: 
```
git clone https://github.com/silgch/Alkemy-Challenge-DAPython.git

```

2) CREAR LA BASE DE DATOS donde se almacenar谩 el contenido. <br>
Por defecto la Base de datos tiene de nombre: "alkemy". Sin embargo, el mismo puede cambiarse modificando en el archivo <b>settings.ini</b> el parametro "DB"

3) CONFIGURAR LOS DATOS DE CONEXION.<br>
Modificar el archivo <b>settings.ini</b> para que la app se conecte a la base de datos. 
Por defecto, se toman los siguientes valores:<br>
       -  HOST = localhost<br>
       -  DB = alkemy<br>
       -  USER = postgres<br>
       -  PASSWORD = postgres<br>
       -  PORT = 5432<br>
       
*IMPORTANTE:* Se pueden modificar los datos de conexion, pero se deben respetar  los nombres de los par谩metros (HOST- DB - USER - PASSWORD - PORT) <br>
Ante la ausencia de alguno de estos, se tomara por defecto los indicados con anterioridad.

4) INSTALAR MODULOS NECESARIOS <br>
Para poder instalar los m贸dulos necesarios para usar  la aplicacion,  solo debes seguir los siguientes pasos:

- INSTALAR EL ENTORNO VIRTUAL:
```
pip install virtualenv
python -m virtualenv myenv

```
(NOTA: Requisito tener instalado PIP)<br>

- ACTIVARLO E INSTALAR LAS DEPENDENCIAS NECESARIAS:


En Windows, ejecuta:
`myenv\Scripts\activate  `<br>
En Unix o MacOS, ejecuta:
`source myenv/bin/activate` <br>
Luego, podras instalar las dependencias necesarias con el siguiente comando: 
`pip install -r requirements.txt`


5) PRIMERA EJECUCION - CREACION DE TABLAS:
Este paso facilitar谩 la creaci贸n de las tablas necesarias para guardar los datos procesados. Solo es necesario en la primera ejecuci贸n.

```
python script.py 

```

6) ACTUALIZACION DE DATOS.
Ejecutando este comando se descargaran la 煤ltima versi贸n de cada archivo fuente, y se actualizar谩 la base de datos.

```
python actualizar.py 

```

## Observaciones 馃憟

Las direcciones  URL de donde  se descargan los archivos fuentes pueden configurarse modificando  el archivo <b>settings.ini</b> en los campos:
- URL_CINES
- URL_MUSEOS
- URL_BIBLIOTECAS




