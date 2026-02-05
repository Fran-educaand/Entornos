#Pilas y Colas
#15. Dada una expresión con paréntesis, verifica si están balanceados usando una pila.

expresion ="((2*3)+4"
pila =[]
correcto = True
for char in expresion:

    if char == "(":
        pila.append (char)
    elif char == ")":
        if not pila:
            correcto = False
        pila.pop()
print ( correcto)


#16. Crear una aplicación que simule una pila de libros. Se mostrará el siguiente menú:

#n: Pide por pantalla el nombre del libro y lo añade a la cima de la pila
#p: Se extrae el libro que está en la cima de la pila y se muestra por pantalla
#l: Muestra un listado de la pila de libros
#b: Borra todos los libros (pidiendo confirmación)
#x: Sale de la aplicación
pila_libros = []


while True:
    print("n: Pide por pantalla el nombre del libro y lo añade a la cima de la pila")
    print("p: Se extrae el libro que está en la cima de la pila y se muestra por pantalla")
    print("l: Muestra un listado de la pila de libros")
    print("b: Borra todos los libros (pidiendo confirmación)")
    print("x: Sale de la aplicación\n")

    resp = input("Elige una opción: ")

    if resp == "n":
        libro = input("Dame el nombre del libro: ")
        pila_libros.append(libro)

    elif resp == "p":
        if pila_libros:
            print("Libro extraído:", pila_libros.pop())
        else:
            print("La pila está vacía.")

    elif resp == "l":
        if pila_libros:
            print("Pila de libros:", pila_libros)
        else:
            print("La pila está vacía.")

    elif resp == "b":
        confirmacion = input("¿Estás seguro de que quieres borrar todos los libros? (s/n): ")
        if confirmacion.lower() == "s":
            pila_libros.clear()
            print("Todos los libros han sido borrados.")
        else:
            print("Operación cancelada.")

    elif resp == "x":
        print("Saliendo de la aplicación.")
        break

    else:
        print("Opción no válida.")




#17. Crear una aplicación que simule un sistema de turnos (médico): se atiende al primero y se añade uno nuevo si llega. Se mostrará el siguiente menú:

#n: Pide por pantalla el nombre del paciente y lo añade como nueva cita
#a: El médico atiende al paciente al que le toca, se muestra por pantalla en nombre del paciente y se saca de las citas pendientes
#l: Muestra un listado de las citas pendientes
#b: Borra todas las citas pendientes (pidiendo confirmación)
#x: Sale de la aplicación

citas_pendientes = []

while True:
    print("n: Pide por pantalla el nombre del paciente y lo añade como nueva cita")
    print("p: El médico atiende al paciente al que le toca, se muestra por pantalla en nombre del paciente y se saca de las citas pendientes")
    print("l: Muestra un listado de las citas pendientes")
    print("b: Borra todas las citas pendientes (pidiendo confirmación)")
    print("x: Sale de la aplicación\n")

    resp = input("Elige una opción: ")

    if resp == "n":
        paciente = input("Dame el nombre del paciente: ")
        citas_pendientes.append(paciente)
    elif resp == "p":
        if citas_pendientes:
            print("Paciente atendido:", citas_pendientes.pop(0))
        else:
            print("No hay citas pendientes.")
    elif resp == "l":
        if citas_pendientes:
            print("Citas pendientes:", citas_pendientes)
        else:
            print("No hay citas pendientes.")
    elif resp == "b":
        confirmacion = input("¿Estás seguro de que quieres borrar todas las citas pendientes? (s/n): ")
        if confirmacion.lower() == "s":
            citas_pendientes.clear()
            print("Todas las citas pendientes han sido borradas.")
        else:
            print("Operación cancelada.")
    elif resp == "x":
        print("Saliendo de la aplicación.")
        break