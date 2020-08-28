"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from Sorting.insertionsort import insertionSort 
from Test.sorting.less_greater import less_count
from Test.sorting.less_greater import greater_count
from Test.sorting.less_greater import less_average
from Test.sorting.less_greater import greater_average


from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas (REQ.3)")
    print("5- Ordenar elementos filtrados por un criterio (REQ.2)")
    print("6- ")
    print("7- Entender las características de un género de películas (REQ. 5)")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter
 
#Laboratorio 2

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element["director_name"].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución",t1_stop-t1_start,"segundos")
    return counter

def orderElementsByCriteria(lst, num_peliculas, mejor_peor, criterio):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """

    lista_nueva=[]
    if criterio.lower()=="count":
        t1_start = process_time()
        if mejor_peor.lower()=="peor":
            insertionSort(lst,less_count)
        else:
            insertionSort(lst, greater_count)
        for peliculas in lst["elements"]:
            if len(lista_nueva)<num_peliculas:
                lista_nueva.append((peliculas["original_title"],peliculas["vote_count"]))
        t1_stop = process_time()
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    else:
        t1_start = process_time()
        if mejor_peor.lower()=="peor":
            insertionSort(lst,less_average)
        else:
            insertionSort(lst, greater_average)
        for peliculas in lst["elements"]:
            if len(lista_nueva)<num_peliculas:
                lista_nueva.append((peliculas["original_title"],peliculas["vote_average"]))
        t1_stop = process_time()
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lista_nueva

#Esta parte es el resto del reto 1
        
def entenderUnGenero(lst, genero):
    """
    Retorna una lista con la cantidad, nombres y promedio de votos de películas de un género dado
    """
    lista_peliculas=[]
    lista_votos=[]
    t1_start = process_time()
    for peliculas in lst["elements"]:
        if genero.lower() in peliculas["genres"].lower():
            lista_peliculas.append(peliculas["original_title"])
            lista_votos.append(int(peliculas["vote_count"]))
    total_votos=0
    for votos in lista_votos:
        total_votos+=votos
    promedio=total_votos/len(lista_votos)
    lista_final=[len(lista_peliculas), lista_peliculas, promedio]
    t1_stop = process_time()
    print(lista_votos)
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lista_final
   
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                print("Datos cargados:",lista['size'],"elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene",lista['size'],"elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else: 
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    column= input("Ingrese la columna de búsqueda\n")
                    counter=countElementsFilteredByColumn(criteria, column, lista) #filtrar una columna por criterio  
                    print("Coinciden",counter,"elementos con el criterio", criteria )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Numero de peliculas:",counter)
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0:
                    print("La lista está vacía")
                else:
                    num_peliculas=int(input("Ingrese el número de películas para su ranking\n"))
                    if num_peliculas<10:
                        print("El número de películas debe ser 10 o más")
                    else:
                        mejor_peor=input("Ingrese si desea su ranking de MEJOR o PEOR\n")
                        criteria = input("Ingrese el criterio COUNT o AVERAGE\n")
                        lista_nueva=orderElementsByCriteria(lista,num_peliculas,mejor_peor,criteria)
                        print("Su lista ordernada es:",lista_nueva)
            elif int(inputs[0])==6: #opcion 6
                if lista==None or lista["size"]==0:
                    print("La lista está vacía")
                else:
                    
            elif int(inputs[0])==7: #opcion 7
                if lista==None or lista["size"]==0:
                    print("La lista está vacía")
                else:
                    genero=input("Ingrese el género a consultar\n")
                    lista_final=entenderUnGenero(lista,genero)
                    print("La cantidad de películas del género", genero,"es:", lista_final[0], ", los nombres de las películas son:", lista_final[1], "y el promedio de votos es:", lista_final[2])
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
    
