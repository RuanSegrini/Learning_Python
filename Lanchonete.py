codigo: int

codigo = int(input("Codigo do produto comprado: "))
quantidade = int(input("Quantidade comprada: "))

if codigo == 1:
    pagar = quantidade * 5
    print(f"Valor a pagar: R${pagar:.2f}")
elif codigo == 2:
    pagar = quantidade * 3.50
    print(f"Valor a pagar: R${pagar:.2f}")
elif codigo == 3:
    pagar = quantidade * 4.80
    print(f"Valor a pagar: R${pagar:.2f}")
elif codigo == 4:
    pagar = quantidade * 8.90
    print(f"Valor a pagar: R${pagar:.2f}")
else:
    pagar = quantidade * 7.32
    print(f"Valor a pagar: R${pagar:.2f}")