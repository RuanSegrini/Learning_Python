x: int
y: int

soma = 0

print(f"Digite dois numeros: ")
x = int(input())
y = int(input())



if x > y:
    for i in range(y + 1, x):
        resto = i % 2
        if resto != 0:
            soma = i + soma

else:
    for i in range(x + 1 , y):
        if i % 2 != 0:
            soma = soma + i


print(f"SOMA DOS IMPARES = {soma}")
