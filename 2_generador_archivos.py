# -*- coding: utf-8 -*-
#Version 0.2 
#Leer archivo Plantilla_Inicial.txt, ordenarlo alfabeticamente, guardar resultado en archivo Plantilla_Final.txt
#Entiende utf-8

import os #importar libreria del sistema operativo
import codecs #importar libreria de codificación para que entienda utf-8

# Parámetros
nombre_archivo_entrada = 'Plantilla_Inicial.txt'
nombre_archivo_salida = 'Plantilla_Final.txt'
CARPETA_ACTUAL = os.path.dirname(os.path.realpath(__file__))
ubicacion_archivos_entrada = os.path.join(CARPETA_ACTUAL, nombre_archivo_entrada) 
ubicacion_archivos_salida = os.path.join(CARPETA_ACTUAL, nombre_archivo_salida)

# Lectura
with codecs.open(ubicacion_archivos_entrada, 'r', 'utf-8') as f:
    contenido =f.read()

# Proceso, ordenarlo alfabéticamente
lineas = contenido.split('\n')
lineas.sort()

# Salida
with codecs.open(ubicacion_archivos_salida, 'w', 'utf-8') as file:
    for item in lineas:
        file.write("%s\n" % item)

		
# Referencias:
################
# https://youtu.be/9bPe0i4uSqQ?t=35m20s Abrir archivos - Python Bucaramanga
# http://stackoverflow.com/a/844443 codificar, decodificar utf-8
################
