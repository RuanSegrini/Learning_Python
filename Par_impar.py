n: int
x: int

n = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, n):
    x = int(input("Digite um numero: "))
    if x % 2 != 0:
        if x < 0:
            print(f"IMPAR NEGATIVO")
        else:
            print(f"IMPAR POSITIVO")
    elif x == 0:
        print(f"NULO")
    else:
        if x < 0:
            print(f"PAR NEGATIVO")
        else:
            print(f"PAR POSITIVO")
    
