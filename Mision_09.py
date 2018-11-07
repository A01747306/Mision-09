# Autor : Saúl Figueroa Conde.
# Matrícula: A01747306.
# Grupo 02.
# Descripción: Éste programa resuelve los ejercicios propuestos que aplican los conocimientos obtenidos acerca del uso
# de listas en python.
#----------------------------------------------------------------------------------------------------------------------
from math import sqrt


# Se declara la función extraerPares que recibe como parámetro una lista de números enteros y regresa una nueva lista
# con los valores pares de la lista original.
def extraerPares(lista):
    nuevaLista = []
    n = len(lista)

    for i in range(0, n):
        if lista[i] % 2 == 0:
            nuevaLista.append(lista[i])

    return nuevaLista


# Se declara la función extraermayoresPrevio que recibe como parámetro una lista y regresa una nueva lista con los
# valores que son mayores a un elemento previo.
def extraerMayoresPrevio(lista):
    nuevaLista = []
    n = len(lista)

    for i in range(0, n-1):
        if lista[i] < lista[i+1]:
            nuevaLista.append(lista[i+1])

    return nuevaLista


# Se declara la función intercambiarParejas que recibe como parámetro una lista de valores y regresa una nueva lista
# con cada pareja de datos intercambiada. Si el número de datos es impar, el último elemento no cambia. La lista
# original no es modificada.
def intercambiarParejas(lista):
    nuevaLista = []
    n = len(lista)

    if n == 0:
        return nuevaLista

    if n == 1:
        nuevaLista.append(lista[0])
        return nuevaLista

    for i in range(1, n, 2):
        nuevaLista.append(lista[i])
        nuevaLista.append(lista[i-1])

    if n % 2 != 0:
        nuevaLista.append(lista[-1])

    return nuevaLista


# Se declara la función intercambiarMM que recibe como parámetro una lista de valores e intercambia el valor menor
# y mayor. Se supone que los valores mayor/menor son únicos. la lista original no se modifica.
def intercambiarMM(lista):
    listaTemporal = []
    index = []
    n = len(lista)
    counter1 = 0
    counter2 = 0

    listaTemporal = lista.copy()
    listaTemporal.sort()

    if n == 0 or n == 1:
        return lista

    if lista == []:
        return lista

    menor = listaTemporal[0]
    mayor = listaTemporal[-1]

    for i in range(0, n):
        if counter1 == 0:
            if lista[i] == menor:
                index.append(i)
                counter1 += 1

    for j in range(0, n):
        if counter2 == 0:
            if lista[j] == mayor:
                index.append(j)
                counter2 += 1

    lista[index[0]] = mayor
    lista[index[1]] = menor

    return lista


# Se declara la función promediarCentro que recibe como parámetro una lista de valores enteros y regresa el promedio
# 'centro' de los valores. El promedio 'centro' se define como el promedio entero de la lista sin considerar el mayor y
# el menor de los datos. Si hay más de un mayor/menor solo se descarta uno.
def promediarCentro(lista):
    nuevaLista = []
    n = len(lista)
    promedio = 0
    suma = 0

    if n == 0 or n == 1 or n == 2:
        promedio = 0
        return promedio

    if lista == []:
        promedio = 0
        return promedio

    nuevaLista = lista.copy()
    nuevaLista.sort()

    nuevaLista.remove(nuevaLista[0])
    nuevaLista.remove(nuevaLista[-1])

    m = len(nuevaLista)

    for i in range(0, m):
        suma += nuevaLista[i]

    promedio = suma//m
    return promedio


# Se declara la función calcularEstadística que recibe como parámetro una lista de números y regresa una dupla con la
# media y la desviación estándar.
def calcularEstadistica(lista):
    n = len(lista)
    suma = 0
    mean = 0
    deviation = 0
    dupla = (0, 0)

    if lista == []:
        return dupla

    for i in range(0, n):
        suma += lista[i]

    suma = suma/n
    mean = suma
    suma = 0

    for j in range (0, n):
        suma += (lista[j] - mean)**2

    deviation = sqrt((suma)/(n-1))
    dupla = (mean, deviation)

    return dupla


# EXTRA: Se declara la función calcularSuma que recibe como parámetro una lista y regresa la suma de los valores
# de la lista. En la suma participan todos los números, excepto los que están al lado de un número 13. (☉_☉)
def calcularSuma(lista):
    n = len(lista)
    listaCopia = lista.copy()
    listaSuma = []
    suma = 0

    if listaCopia == []:
        suma = 0
        return suma

    listaCopia.insert(0, 0)
    listaCopia.append(0)

    m = len(listaCopia)

    if listaCopia[0] != 13:
        listaSuma.append(listaCopia[0])

    if listaCopia[-1] != 13:
        listaSuma.append(listaCopia[-1])

    for i in range(1, m-1):
        if listaCopia[i] != 13 and (listaCopia[i+1]) != 13 and (listaCopia[i-1]) != 13:
            listaSuma.append(listaCopia[i])

    listaSuma.remove(listaSuma[0])
    listaSuma.remove(listaSuma[0])
    n = len(listaSuma)

    for j in range(0, n):
        suma += listaSuma[j]

    return suma


# Se declara la función main que prueba cada uno de los casos con distintas valores determinados para las listas que se
# enviarán a las funciones.
def main():
   list1 = [22, 45]
   list2 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
   list3 = [0, 9, 0, 8, 8, 10]
   list4 = [5]
   list5 = []
   list6 = [0, 0, 0, 0, 0]
   list7 = [-2, -4, -6, -7, -12]

   nuevaLista1 = extraerPares(list1)
   nuevaLista2 = extraerPares(list2)
   nuevaLista3 = extraerPares(list3)
   nuevaLista4 = extraerPares(list4)
   nuevaLista5 = extraerPares(list5)
   nuevaLista6 = extraerPares(list6)
   nuevaLista7 = extraerPares(list7)

   print("Problema 1. Regresa una lista con los valores pares de la lista original.")

   print("Con la lista {}, regresa {}".format(list1, nuevaLista1))
   print("Con la lista {}, regresa {}".format(list2, nuevaLista2))
   print("Con la lista {}, regresa {}".format(list3, nuevaLista3))
   print("Con la lista {}, regresa {}".format(list4, nuevaLista4))
   print("Con la lista {}, regresa {}".format(list5, nuevaLista5))
   print("Con la lista {}, regresa {}".format(list6, nuevaLista6))
   print("Con la lista {}, regresa {}".format(list7, nuevaLista7))

   print("")

   nuevaLista1 = extraerMayoresPrevio(list1)
   nuevaLista2 = extraerMayoresPrevio(list2)
   nuevaLista3 = extraerMayoresPrevio(list3)
   nuevaLista4 = extraerMayoresPrevio(list4)
   nuevaLista5 = extraerMayoresPrevio(list5)
   nuevaLista6 = extraerMayoresPrevio(list6)
   nuevaLista7 = extraerMayoresPrevio(list7)

   print("Problema 2. Regresa una lista con los valores mayores a un elemento previo.")

   print("Con la lista {}, regresa {}".format(list1, nuevaLista1))
   print("Con la lista {}, regresa {}".format(list2, nuevaLista2))
   print("Con la lista {}, regresa {}".format(list3, nuevaLista3))
   print("Con la lista {}, regresa {}".format(list4, nuevaLista4))
   print("Con la lista {}, regresa {}".format(list5, nuevaLista5))
   print("Con la lista {}, regresa {}".format(list6, nuevaLista6))
   print("Con la lista {}, regresa {}".format(list7, nuevaLista7))

   print("")

   nuevaLista1 = intercambiarParejas(list1)
   nuevaLista2 = intercambiarParejas(list2)
   nuevaLista3 = intercambiarParejas(list3)
   nuevaLista4 = intercambiarParejas(list4)
   nuevaLista5 = intercambiarParejas(list5)
   nuevaLista6 = intercambiarParejas(list6)
   nuevaLista7 = intercambiarParejas(list7)

   print("Problema 3. Regresa una lista con cada pareja de datos intercambiada.")

   print("Con la lista {}, regresa {}".format(list1, nuevaLista1))
   print("Con la lista {}, regresa {}".format(list2, nuevaLista2))
   print("Con la lista {}, regresa {}".format(list3, nuevaLista3))
   print("Con la lista {}, regresa {}".format(list4, nuevaLista4))
   print("Con la lista {}, regresa {}".format(list5, nuevaLista5))
   print("Con la lista {}, regresa {}".format(list6, nuevaLista6))
   print("Con la lista {}, regresa {}".format(list7, nuevaLista7))

   print("")

   list1 = [5, 9, 3, 22, 19, 31, 10, 7]
   list2 = [1, 2, 3]
   list3 = [0, 9, 0, 8, 8, 10]
   list4 = [5]
   list5 = []
   list6 = [0, 0, 0, 0, 0]
   list7 = [-2, -4, -6, -7, -12]

   list1 = intercambiarMM(list1)
   list2 = intercambiarMM(list2)
   list3 = intercambiarMM(list3)
   list4 = intercambiarMM(list4)
   list5 = intercambiarMM(list5)
   list6 = intercambiarMM(list6)
   list7 = intercambiarMM(list7)

   print("Problema 4. Intercambia el valor menor y mayor.")

   print("La lista queda así: {}".format(list1))
   print("La lista queda así: {}".format(list2))
   print("La lista queda así: {}".format(list3))
   print("La lista queda así: {}".format(list4))
   print("La lista queda así: {}".format(list5))
   print("La lista queda así: {}".format(list6))
   print("La lista queda así: {}".format(list7))

   print("")

   list1 = [70, 80, 90]
   list2 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
   list3 = [20, 55, 30, 5, 55, 5]
   list4 = [5, 9, 1, 8]
   list5 = [5, 8]
   list6 = []
   list7 = [1]

   promedio1 = promediarCentro(list1)
   promedio2 = promediarCentro(list2)
   promedio3 = promediarCentro(list3)
   promedio4 = promediarCentro(list4)
   promedio5 = promediarCentro(list5)
   promedio6 = promediarCentro(list6)
   promedio7 = promediarCentro(list7)

   print("Problema 5. Regresa el promedio centro.")

   print("Con la lista {}, regresa {}".format(list1, promedio1))
   print("Con la lista {}, regresa {}".format(list2, promedio2))
   print("Con la lista {}, regresa {}".format(list3, promedio3))
   print("Con la lista {}, regresa {}".format(list4, promedio4))
   print("Con la lista {}, regresa {}".format(list5, promedio5))
   print("Con la lista {}, regresa {}".format(list6, promedio6))
   print("Con la lista {}, regresa {}".format(list7, promedio7))

   print("")

   list1 = [1, 2, 3, 4, 5, 6]
   list2 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
   list3 = []

   dupla1 = calcularEstadistica(list1)
   dupla2 = calcularEstadistica(list2)
   dupla3 = calcularEstadistica(list3)

   print("Problema 6. Regresa una dupla con la media y la desviación estandar.")

   print("Con la lista {}, regresa {}".format(list1, dupla1))
   print("Con la lista {}, regresa {}".format(list2, dupla2))
   print("Con la lista {}, regresa {}".format(list3, dupla3))

   print("")

   list1 = [1, 2, 3, 4, 5, 6]
   list2 = [5, 2, 13, 4, 1, 6, 1, 8, 4, 1, 5]
   list3 = [5, 2, 13, 4, 1, 6, 1, 8, 4, 13, 1]
   list4 = [13, 49]
   list5 = []

   suma1 = calcularSuma(list1)
   suma2 = calcularSuma(list2)
   suma3 = calcularSuma(list3)
   suma4 = calcularSuma(list4)
   suma5 = calcularSuma(list5)

   print("[EXTRA]Problema 7. Regresa la suma de los valores de la lista (No participan los números a lado de un '13').")

   print("Con la lista {}, regresa {}".format(list1, suma1))
   print("Con la lista {}, regresa {}".format(list2, suma2))
   print("Con la lista {}, regresa {}".format(list3, suma3))
   print("Con la lista {}, regresa {}".format(list4, suma4))
   print("Con la lista {}, regresa {}".format(list5, suma5))

   print("")
   salir = input("Presione enter para salir...")
   print("")


# Se llama a la función main para empezar a correr el programa.
main()