'''1. Realizar un programa que muestre un menú con las siguientes opciones:
1 Suma
2 Resta
3 Multiplicación
4 División
0 Salir'''

'''A continuación solicitará 2 números y mostrará el resultado de la elegida.
El programa se repetirá continuamente hasta que el usuario seleccione la opción de salir'''

while True:
    n1 = int(input("Dame un numero"))
    n2 = int(input("Dame otro numero"))

    resp =input("Elige una opcion \n1. Suma\n2 Resta\n3 Multiplicación\n5 División\n0 Salir\n")
    match int(resp):
        case 1: print (n1+n2)
        case 2: print (n1-n2)
        case 3: print (n1*n2)
        case 4: print (n1/n2)
        case 0: break

'''2. Realizar un programa que convierta grados Celsius a Fahrenheit'''
temp = int(input ("Dame la temperatura en celsius"))
fah = (temp*1.8)+32
print (fah)

'''3. Suponiendo que tu nombre está en una variable llamada nombre, realiza solo una llamada a
la función print para obtener los siguientes resultados
a) Hola, me llamo <nombre>
b) <nombre> repetido 5 veces separadas por el caracter "*"'''

nombre = "Fran"
print(f"Hola, me llamo {nombre}")
print(f"{nombre}*"*4 +f"{nombre}")

'''4. Imprimir por pantalla las siguientes cadenas de caracteres:
a) I'm a student
b) "I'm a student"
c) Es difícil escribir 'una cadena con el carácter" '''

print("i'm a student")
print('"i\'m a student"')
print (' Es dificil escribir \' una cadena con el caracter" \'')


'''5. Verifica si un número introducido es mayor que 10'''

num = int (input ("Pon un numero"))

if num >10:
    print ("Es mayor que diez")
else: print("Es menor o igual a diez")

'''6. Pide una edad y comprueba si la persona es mayor de edad y no supera 65'''

edad = int(input("Dime tu edad: "))
if edad >18 and edad < 66:
    print("Es mayor de edad pero menor de 66 ")
elif edad > 18 and edad > 65:
    print("Es mayor de edad y mayor de 65 años ")
else:print("Es menor de edad")


'''7. Escribe una expresión que determine si una contraseña es válida cuando:
• Tiene más de 8 caracteres
• Contiene la letra "@"

• No contiene espacios'''

contraseña = "holaquetal@"

if " " not in contraseña and "@" in contraseña and len(contraseña) > 8:
    print("contraseña valida")
else: print ("Contraseña invalida")


'''8. Dada la cadena "pythonista":
• Muestra la primera letra
• Muestra la última
• Muestra la letra con índice 4'''

palabra = "pythonista"

print(palabra[1])
print(palabra[-1])
print(palabra[4])


'''9. Pide una cadena de caracteres por teclado e imprímela en 2 líneas dividida por la mitad. No
se pueden usar bucles. Por ejemplo, la cadena "casa" daría como resultado
ca
sa
Y la cadena "remar" daría
rem
ar'''

cadena = input("Escribe... ")
mitad = len(cadena)/2
print(cadena[:mitad])
print(cadena[mitad:])

'''10. Toma una frase y crea una nueva cadena donde las letras en índice par estén en minúscula y
as de índice impar en mayúscula.'''




'''11. Declara variables de todos los tipos que hemos estudiado y muestra por pantalla para cada
una de ellas:
La variable <nombre de la vble> vale <valor de la vble> y es de tipo <tipo de la vble>'''



'''12. Dado un valor en segundos, usa variables para calcular horas, minutos y segundos'''