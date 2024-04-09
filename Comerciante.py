lucro_total: float
total_venda: float
total_compra: float
lucro_acima: int
lucro_medio: int
lucro_abaixo: int
x: int
n: int

x = 0
total_compra = 0
total_venda = 0
lucro_abaixo = 0
lucro_medio = 0
lucro_acima = 0

n = int(input("Sera digitados dados de quantos produtos? "))

compra: [float] = [0 for x in range(n)]
venda: [float] = [0 for x in range(n)]
nome: [str] = [0 for x in range(n)]
porcentagem: [float] = [0 for x in range(n)]

for i in range(n):
    x += 1
    print(f"Produto {x}: ")
    nome[i] = input("Nome: ")
    compra[i] = float(input("Preco de compra: "))
    venda[i] = float(input("Preco de venda: "))

    total_compra = total_compra + compra[i]
    total_venda = total_venda + venda[i]

for i in range(n):
    porcentagem[i] = round((venda[i] - compra[i]) / compra[i] * 100, 2)

for i in range(n):

    if porcentagem[i] < 10:
        lucro_abaixo += 1

    elif porcentagem[i] <= 20:
        lucro_medio += 1

    else:
        lucro_acima += 1


lucro_total = total_venda - total_compra

print(f"RELATORIO:")
print(f"Lucro abaixo de 10% = {lucro_abaixo}")
print(f"Lucro entre 10% e 20% = ", lucro_medio)
print(f"Lucro acima de 20% = ", lucro_acima)
print(f"Valor total de compra =", total_compra) 
print(f"Valor total de venda =", total_venda) 
print(f"Lucro total =", lucro_total) 

