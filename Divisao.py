n: float
x: int
y: int
divisao: float

n = int(input("Quantos casos voce vai digitar? "))

for i in range(0, n):
    x = int(input("Entre com o numerador: "))
    y = int(input("Entre com o denominador: "))

    if y == 0:
        print(f"DIVISAO IMPOSSIVEL!")
    else:
        divisao = x / y
        print(f"DIVISAO = {divisao:.2f}")