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

frase = ("Hola que tal")
frasn = (" ")
for i , valor in enumerate (frase):
    
    if i % 2 == 0:
        frasn+=valor.lower()
    else:
        frasn+=valor.upper()

print(frasn)

'''11. Declara variables de todos los tipos que hemos estudiado y muestra por pantalla para cada
una de ellas:
La variable <nombre de la vble> vale <valor de la vble> y es de tipo <tipo de la vble>'''

inte = 12
floatin = 1.1
frase = "Hola"
bol = True

print(f"La variable inte vale {inte} y es de tipo {type(inte)}")
print(f"La variable floatin vale {floatin} y es de tipo {type(floatin)}")
print(f"La variable frase vale {frase} y es de tipo {type(frase)}")
print(f"La variable inte vale {bol} y es de tipo {type(bol)}")



'''12. Dado un valor en segundos, usa variables para calcular horas, minutos y segundos'''
tiempo = 5000
horas = 0
minutos = 0
segundos = 0

if tiempo >= 60:
     minutos= tiempo //60
     minutos = minutos %60
else:segundos = tiempo 

if minutos >= 60:
     horas = minutos //60
     minutos = minutos %60

'''13. Calcula si un año introducido por teclado es bisiesto (los divisibles por 4 excepto los que
también sean divisibles por 100 o por 400)'''

año = 3000

if año % 4 ==0 and año % 100 != 0 and año % 400 != 0:
    print("Es bisiesto")
else:
    print ("No bisiesto")

'''14. Dado un número, comprueba si su valor absoluto es mayor que 10 sin usar abs()'''

numero =2.5


'''15. Compara tres números y determina cuál es el mayor usando solo operadores relacionales'''

num1 = 10
num2 = 2
num3= 4

if num1 > num2:
    if num1 > num3:
        print (f"{num1}")
    else: print(num3)
elif(num2 > num3):
    print (num2)
else:print(num3)

'''16. Comprueba si un número es par o múltiplo de 5 usando or'''

num = 10

if num%2==0 or num%5==0:
    print("Bien")




'''17. Escribe un programa que pregunte si llueve y si tienes paraguas, y determine si puedes salir
(usa lógica)'''

llueve= input ("Llueve?")

if llueve == "si":
    paraguas = ('Llevas paraguas?')
    if paraguas == "si":
        print("Sal")
    else:print("Coje uno y sal")
else:print("No salgas")

'''18. Realiza un desplazamiento a la izquierda: calcula 7 << 2 y explica el resultado'''

print(7<<2) #111
print(28) #11100


'''19. Realiza un desplazamiento a la derecha: calcula 20 >> 3'''

print(20>>3) # 10100 >> #00010



'''20. Aplica el operador NOT (~) a 0b1010 y muestra el resultado en binario usando una máscara
de 4 bits'''

# Si queremos usar el operador ~ para invertir sin complemento a 2 necesitamos usar máscaras
n = ~ 0b101
bits = 3

mask = (1 << bits) - 1   # 0b111
r = ~n & mask            # invierto y recorto a 3 bits

print(f"{r:b}")   # 010




'''21. Escribe un programa que determine si el bit menos significativo de un número es 1 (el menos
significativo es el que está más a la derecha)'''

num = 0b10101010

if num & 1 == 1:
    print ("par")
else:print("impar")

#cuarto digito

explicanum = 0b10101010  # 170

# Desplazamos 3 posiciones a la derecha
bit = (explicanum >> 3) & 1

if bit == 1:
    print("El cuarto bit es 1")
else:
    print("El cuarto bit es 0")