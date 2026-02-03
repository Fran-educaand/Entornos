#Listas
#1. Crea una lista con 10 enteros y calcula la suma total sin usar sum().
lista = [1,2,3,4,5,6,7,8,9,10]
suma = 0  
for num in lista:
    suma +=num
print(suma)

#2. Dada una lista de nombres, cuenta cuántos empiezan por vocal.
listan= ['Antonio','Lucas','Alvaro']
contador = 0
vocales = 'AEIOUaeiou'
for nombre in listan:
    if nombre[0] in vocales:
        contador += 1
print(contador)

#3. Dada una lista de números, crea otra lista con solo los pares

lista2  = [23,3,45,565,78,74,433,221,2]
listap =[]

for num in lista2:
    if num %2 == 0:
        listap.append(num)
print(listap)

#4. Elimina de una lista todas las apariciones de un valor dado (ej. borrar todos los 0).

valor = int(input("Escribe un numero:"))

if valor in lista2:
    for ind , num in enumerate (lista2):
        if num == valor:
            del lista2[ind]
else: print("El valor no está en la lista")
print (lista2)

#5. Dada una lista, rota sus elementos 1 posición a la derecha (el último pasa a ser el primero).
lista3 = [1,2,3,4,5]
ultimo = lista3.pop()
lista3.insert(0, ultimo)
print(lista3)

#6. Genera una lista con los primeros n múltiplos de 3.
n = int(input("Dame un numero: "))
lista3 = []
for num in range(1,n+1):
    lista3.append(num*3)
print(lista3)

#7. Dada una lista con números repetidos, crea una lista que conserve el orden pero sin repetidos.

listar=[1,2,3,4,4,5,6,6]
lista4=[]
for ind, num in enumerate(listar):
    if num in lista4:
        pass
    else: lista4.append(num)
print(lista4)
    
#8. Dada una lista, obtén una sublista con los elementos del índice 3 al 7 (incluido 7).
lista5 = [10,20,30,40,50,60,70,80,90,100]
sublista = lista5[3:8]
print(sublista)
#9. Dada una lista, obtén los 5 últimos elementos usando slicing.
lista6 = [5,10,15,20,25,30,35,40,45,50]
ultimos5 = lista6[-5:]
print(ultimos5)

#10. Dada una lista, crea una sublista con un salto de 3 en 3 elementos.
lista7 = [1,2,3,4,5,6,7,8,9,10,11,12]
sublista3 = lista7[::3]
print(sublista3)

#11. Dada una lista, reemplaza con 0 el tramo entre índices 4 y 8 usando slicing.
lista8 = [10,20,30,40,50,60,70,80,90,100]
lista8[4:9] = [0]*5
print(lista8)
