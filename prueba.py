c = "pythonista"
for i in range(len(c)):
  print(c[-1-i], end="")
print()

print(c[::-1])



print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")


a=0b101 & 0b111
print(a)
print(f"{a:b}")

a=0b101 | 0b111
print(f"{a:b}")

# Si queremos usar el operador ~ para invertir sin complemento a 2 necesitamos usar máscaras
n = 0b101
bits = 3

mask = (1 << bits) - 1   # 0b111
r = ~n & mask            # invierto y recorto a 3 bits

print(f"{r:b}")   # 010