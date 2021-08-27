#Tarea 2 Manejo de Máquinas Virtuales
#Marcia Cocozza Barrantes 2016004618
#Gabriel Devandas Mata 2016082713

#Librerias importadas.
from multiprocessing import Process
import multiprocessing
import time
import random
import argparse
import os

#Extracción de la ubicación del archivo .py
#para utilizar al guardar el txt.
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#Lista de valores iniciada.
t = []

#Configuración de los argumentos de entrada por medio de argparse.
parser = argparse.ArgumentParser(description='Tarea 2')
parser.add_argument('longitud', metavar='N', type=int, nargs='+',
                    help='Tamaño del array')
parser.add_argument('formato', metavar='F', type=int, nargs='+',
                    help='imprimir en txt o en consola')
args = parser.parse_args()

#Variables a utilizar, extraidas de los parametros.
n = args.longitud[0]
f = args.formato[0]

#Variables que dividen el array en 4 partes para el proceso
#multihilo.

ran1 = n//4
ran2 = n//2
ran3 = ran1 + ran2


#Función principal que calcula la potencia de cada elemento del array.
def calculo (t, inicio, final):
    for i in range(inicio, final):
        y = t[i] ** 2


if __name__ == '__main__':

    #Llena el array con n valores random entre -100 y 100.
    for i in range(n):
        t.append(random.randint(-100, 100))

    #Inicia un pool de procesos para la ejecución a 4 hilos.
    pool = multiprocessing.Pool(4)

    #Conteo de tiempo para un hilo.
    inicio_unhilo = time.time()

    calculo(t, 0, n)

    tiempo_unhilo = time.time() - inicio_unhilo

    #Conteo de tiempo para multihilo.
    inicio_multihilo = time.time()

    #Inicia el pool de procesos con la función a ejecutar.
    pool.apply_async(calculo, args=(t, 0, n))
    pool.close
    pool.join

    tiempo_multihilo = time.time() - inicio_multihilo

    #Condicional para el argumento de impresión en consola
    #o guardar en .txt .
    if f == 0:
        print("Tiempo a un hilo: ", tiempo_unhilo)
        print("Tiempo a 4 hilos: ", tiempo_multihilo)

    else:
        archivo = open(os.path.join(__location__, "Tarea2.txt"), "w")
        archivo.write("Tiempo a un hilo: "+str(tiempo_unhilo)+"\n")
        archivo.write("Tiempo a 4 hilos: "+str(tiempo_multihilo))
        archivo.close()