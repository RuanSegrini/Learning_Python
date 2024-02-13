minutos: int
pagar: float

minutos = int(input("Digite a quantidade de minutos: "))

if minutos <= 100:
    print(f"Valor a pagar: R$50.00")

else:
    pagar = ((minutos - 100) * 2) + 50
    print(f"Valor a pagar: R${pagar:.2f}")