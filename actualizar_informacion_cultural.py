from config import cargar_configuracion_inicial
from etl import get_archivos_fuentes


if __name__ == '__main__':
    cargar_configuracion_inicial()
    get_archivos_fuentes()



