import pandas as pd
from decouple import config
import requests
from  os.path  import exists
from os import makedirs
from datetime import datetime
import logging

# Funciones necesario para el proceso ETL.


# ---------------- EXTRACT  ----------------
def get_archivos_fuentes():
    ''' Obtener los archivos fuentes.
    Descarga todos los archivos fuente de las URL configuradas en el archivo "settings.ini".
    Almacena los mismos de forma local, siguiendo la siguiente estructura: “categoría\año-mes\categoria-dia-mes-año.csv”
    '''
    url_cines=config('URL_CINES')
    url_bibliotecas=config('URL_BIBLIOTECAS')
    url_museos=config('URL_MUSEOS')

    logging.info('Leyendo Config URL_CINES: %s' , url_cines)
    logging.info('Leyendo Config URL_BIBLIOTECAS: %s', url_bibliotecas)
    logging.info('Leyendo Config URL_MUSEOS: %s', url_museos)

    try:
        descargar_archivo(url_cines,"cines" )
        descargar_archivo(url_bibliotecas,"bibliotecas" )
        descargar_archivo(url_museos,"museos" )
    except:
        logging.error("[OBTENER ARCHIVOS FUENTE] No se pudo completar la descarga de archivos")


def procesar_datos():
    pass

def descargar_archivo(remote_url, categoria):
    '''Descargar Archivo.

    Argumentos:
    remote_url  -- URL de la cual de descargará el archivo.
    categoria   -- Categoria correspondiente al archivo a descargar.

    Los archivos son organizados en rutas siguiendo la siguiente estructura: “categoría\año-mes\categoria-dia-mes-año.csv”
    Si el archivo existe lo  reemplaza. La fecha de la nomenclatura es la fecha de descarga.
    ''' 
    response= requests.get(remote_url)
    filename = get_filename(categoria)

    if(response.status_code == 200):
        response.encoding=response.apparent_encoding
        #response.encoding= 'UTF-8' 
        with open(filename, 'wb') as  file:
            file.write(response.content)
        logging.info('[OBTENER ARCHIVOS FUENTE %s] Archivo descargado  Ruta:%s URL:%s', categoria.upper(),  filename, remote_url)
    else:
        logging.error('[OBTENER ARCHIVOS FUENTE %s] No se pudo descargar  Ruta:%s URL:%s', categoria.upper(),filename, remote_url)
    

def get_filename(categoria):
    '''Obtener nombre del archivo.

    Argumentos:
    categoria -- Categoria del archivo. 

    El nombre del archivo seguira la estructura: “categoría\año-mes\categoria-dia-mes-año.csv”
    '''
    fecha=datetime.now().strftime
    #Path ejemplo: “museos\2021-noviembre\”
    path = str(categoria + '/' + fecha("%Y") + "-" +  fecha("%B"))
    if not exists(path):
        makedirs(path)
        logging.debug("[PATH LOCAL CREADO] Path: %s", path)
    # Ejemplo a retornar:“museos\2021-noviembre\museos-03-11-2021”
    return str(path + '/' + categoria + '-' + fecha("%d")  + "-" + fecha("%m")  + "-" + fecha("%Y")  + '.csv')

    # ---------------- TRANSFORM  ----------------



    # ---------------- LOAD  ----------------