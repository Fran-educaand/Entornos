#18. Dada una lista de pares (tuplas) (nombre, edad), encuentra la edad máxima.

personas = [("Ana", 20), ("Luis", 35), ("Marta", 29)]
'''1'''
edad_maxima = max(edad for nombre, edad in personas)
print(edad_maxima)

'''2'''
mayor = max(personas, key=lambda x:x[1])
print(mayor)
persona,edad = mayor
print(f"L a persona mas mayor es {persona} y  la edad es {edad}")

#19. Dada una tupla de números, crea otra tupla con solo los positivos.
numeros = (-2, 3, -1, 5, -4, 6)
positivos = tuple(num for num in numeros if num > 0)
print(positivos)

#20. Intercambia los valores de dos variables usando tuplas (sin variable auxiliar).
a = 5
b = 10

a, b = b, a

print(a, b)

#21. Dada una lista de tuplas (producto, precio), ordena por precio sin modificar el formato.
productos=[('manzanas',12), ('pera',13), ('cebolla',5)]
ordenado=sorted(productos,key=lambda x:x[0],reverse=True)
print(ordenado)
print( )

#22. Crear una aplicación que funcione como un diccionario español-inglés. Mostrará un menú con
#las siguientes opciones:

#-n: pide la palabra en español y la traducción al inglés y las guarda en el diccionario
#-t: pide una palabra en español y muestra la traducción al inglés. Si no existe muestra un error
#-b: pide una palabra en español y la borra del diccionario. Si la palabra no existe dará un error
#(pide confirmación)
#-c: modifica una entrada del diccionario pidiendo la palabra en español e inglés. Si la palabra
#no existe dará un error
#-e: lista todas las palabras en español
#-i: lista todas las palabras en inglés
#-l: lista en una tabla todas las palabras en español y en inglés
#-x: elimina todas las palabras del diccionario (pidiendo confirmación)
#-0: sale de la aplicación

print('''        BIENVENIDO AL DICCIONARIO
-n: pide la palabra en español y la traducción al inglés y las guarda en el diccionario
-t: pide una palabra en español y muestra la traducción al inglés. Si no existe muestra un error
-b: pide una palabra en español y la borra del diccionario. Si la palabra no existe dará un error
(pide confirmación)
-c: modifica una entrada del diccionario pidiendo la palabra en español e inglés. Si la palabra
no existe dará un error
-e: lista todas las palabras en español
-i: lista todas las palabras en inglés
-l: lista en una tabla todas las palabras en español y en inglés
-x: elimina todas las palabras del diccionario (pidiendo confirmación)
-0: sale de la aplicación
''')

dicci={}
opcion=("Elige una opcion: ")
match opcion:
    case "n":
        esp=str("Escribe una palabra en español: ")
        ing=str("Escribe su traduccion: ")
        dicci[esp]=ing
    case "t":
        esp=str("Escribe una palabra en español: ")
        if esp in dicci:
            print(dicci[esp])
        else:
            print("Error, la palabra no existe")
    case "b":
        esp=str("Escribe una palabra en español: ")
        if esp in dicci:
            confirmacion=str("¿Estas seguro de que quieres eliminar esta palabra? (s/n): ")
            if confirmacion.lower() == "s":
                del dicci[esp]
                print("Palabra eliminada")
            else:
                print("Operación cancelada")
        else:
            print("Error, la palabra no existe")
    case "c":
        esp=str("Escribe una palabra en español: ")
        if esp in dicci:
            ing=str("Escribe su nueva traduccion: ")
            dicci[esp]=ing
            print("Entrada modificada")
        else:
            print("Error, la palabra no existe")
    case "e":
        print("Palabras en español:")
        for palabra in dicci.keys():
            print(palabra) 
    case "i":
        print("Palabras en inglés:")
        for palabra in dicci.values():
            print(palabra)
    case "l":
        print("Palabra en español | Palabra en inglés")
        print("-" * 30)
        for esp, ing in dicci.items():
            print(f"{esp:20} | {ing}")
    case "x":
        confirmacion=str("¿Estas seguro de que quieres eliminar todas las palabras? (s/n): ")
        if confirmacion.lower() == "s":
            dicci.clear()
            print("Todas las palabras han sido eliminadas")
        else:
            print("Operación cancelada")
    case "0":
        print("Saliendo de la aplicación...")
