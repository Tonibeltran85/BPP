'''Haciendo uso de comprensión de listas realice un programa que, dado 
una lista de listas de números enteros, devuelva el máximo de cada 
lista. Por ejemplo, suponga la siguiente listas de listas:
[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
El programa debe devolver el mayor elemento de cada sublista 
(señalado en negrita).
Ahora, haciendo uso del pdb, inserte puntos de parada justo en la línea 
donde ha implementado la compresión de listas. Haga pruebas 
mostrando el contenido de las variables y continuar con la ejecución 
línea a línea. ¿Qué conclusiones obtiene?

'''
import random
import pdb
pdb.set_trace()

listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
maximo = [max(lista) for lista in listas]
print("Numero Maximos de la lista de listas: ",maximo)

'''
2. Haga uso de la función filter para construir un programa que, dado 
una lista de n números devuelva aquellos que son primos. Por 
ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente 
debe devolver como resultado [3, 5, 5, 13]'''

def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

n = input("Introduce un número n para el tamañaño de la lista: ")

lista = [random.randint(0,100) for i in range(int(n))]
print("lista de numeros a comprobar: ", lista)
listaFilter = list(filter(lambda x: es_primo(x), lista))
print("Numero Primos: ", listaFilter)


lista = [3, 4, 8, 5, 5, 22, 13]
print("Segunda lista de numeros a comprobar: ", lista)
listaFilter2 = list(filter(lambda x: es_primo(x), lista))
print("Numero Primos: ", listaFilter2)