import logging
from locale import setlocale
from locale import LC_ALL

def cargar_configuracion_inicial():
    ''' Configuración Necesaria para la correcta ejecucion del programa.
        Incluye configuración del logging. 
    '''

    # Configuracion del logging
    #FORMAT = '%(asctime)s  %(message)s'
    logging.basicConfig(format='%(asctime)s    %(levelname)s    %(message)s', filename='actualizacion_informacion_cultural.log', level='DEBUG',  datefmt='%m/%d/%Y %I:%M:%S %p')
    setlocale(LC_ALL, 'es_ES')
    logging.info('Configuración Inicial realizada.')


    # logging.critical('Critical de prueba')
    # logging.error('Error prueba')
    # logging.warning('warning prueba')
    # logging.debug('Debug prueba') 