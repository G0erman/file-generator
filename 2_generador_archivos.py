#Version 0.1 
#Leer archivo Plantilla_Inicial.txt, ordenarlo alfabeticamente, guardar resultado en archivo Plantilla_Final.txt

import os #importar libreria del sistema operativo

# Parámetros
nombre_archivo_entrada = 'Plantilla_Inicial.txt'
nombre_archivo_salida = 'Plantilla_Final.txt'
CARPETA_ACTUAL = os.path.dirname(os.path.realpath(__file__))
ubicacion_archivos_entrada = os.path.join(CARPETA_ACTUAL, nombre_archivo_entrada) 
ubicacion_archivos_salida = os.path.join(CARPETA_ACTUAL, nombre_archivo_salida)

# Lectura
with open(ubicacion_archivos_entrada, 'r') as f:
    contenido =f.read()

# Proceso, ordenarlo alfabéticamente
lineas = contenido.split('\n')
lineas.sort()

# Salida
with open(ubicacion_archivos_salida, 'w') as file:
    for item in lineas:
        file.write("%s\n" % item)

		
# Referencias:
################
# https://youtu.be/9bPe0i4uSqQ?t=35m20s Abrir archivos - Python Bucaramanga
################
