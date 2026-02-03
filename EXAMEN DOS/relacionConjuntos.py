#Conjuntos
#12. Dadas 2 listas calcula la unión, intersección y diferencia
conj1 = {1,2,3,4,5,6}
conj2 = {4,5,6,7,8,9}

print("Unión:", conj1 | conj2)
print("Intersección:", conj1 & conj2)  
print("Diferencia:", conj1 - conj2)

#13. Dada una lista de números, cuenta cuántos valores distintos hay usando un conjunto.
lista = [1,2,2,3,4,4,5,6,7,7,8,9]
conjunto = set(lista)
print("Cantidad de valores distintos:", len(conjunto))

#14. Dadas dos listas, elimina de la primera los elementos que aparezcan en la segunda usando sets.

lista1 = [1,2,3,4,5,6,7]
lista2 = [5,6,7,8,9,10]

conj1 = set(lista1)
conj2 = set(lista2)

conj1 = conj1 -conj2
print(conj1)
