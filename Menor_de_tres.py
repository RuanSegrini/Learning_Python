valor1: int
valor2: int
valor3: int

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
    print(f"MENOR = {valor1}")

elif valor2 < valor1 and valor2 < valor3:
    print(f"MENOR = {valor2}")

else:
    print(f"MENOR = {valor3}")