unitario: float
quantidade: int
recebido: float
preco: float
troco: float

unitario = float(input("Preço unitario do produto: "))
quantidade = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))

preco = (unitario * quantidade)

if preco > recebido:
    troco = preco - recebido
    print(f"DINHEIRO INSUFICIENTE. FALTAM {troco:.2f} reais")

else:
    troco = recebido - preco
    print(f"TROCO = {troco:.2f}")