n: int
x: int
dentro: int
fora: int

dentro = 0
fora = 0

n = int(input("Quantos numeros voce vai digitar: "))

for i in range(0, n):
    x = int(input("Digite um numero: "))
    if x >= 10 and x <= 20:
        dentro += 1

    else:
        fora += 1

print(f"DENTRO = {dentro}")
print(f"FORA = {fora}")

