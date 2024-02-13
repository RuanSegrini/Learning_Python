preco: float
quantidade: int
recebido: float
troco: float

preco = float(input("Preço unitario do produto: "))
quantidade = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))

troco = recebido - (preco * quantidade)

print(f"TROCO = {troco:.2f}")