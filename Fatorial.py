n: int
fatorial: int
contador: int

contador = 0
fatorial = 1

n = int(input("Digite o valor de N: "))

for i in range(1, n + 1):
    if n == 0:
        print(f"FATORIAL = 1")
    elif n == 1:
        print(f"FATORAIL = 1")
    else:
        
        fatorial *= i

print(f"FATORIAL = {fatorial}")