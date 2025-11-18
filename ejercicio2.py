h = "Hola que tal"




for i  in range(1,len(h)+1):
  
        print(h[-i],end=" ")

cadena = input(" escribe")

for i,valor in enumerate(cadena):
    if i % 2 == 0:
        print(valor.upper(),end="")
    else: print(valor.lower(),end="")
print()
print("Fin del programa")