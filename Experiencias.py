n: int
C: int
R: int
S: int
tipo: str

C = 0
S = 0
R = 0

n = int(input("Quantos casos serao digitados? "))

for i in range(0, n):
    
    quantidade = int(input("Quantidades de cobaias: "))
    tipo = input("Tipo de cobaia: ")

    if tipo == 'C':
        C = quantidade + C

    elif tipo == 'R':
        R = quantidade + R

    elif tipo == 'S':
        S = quantidade + S

total = R + S + C
percentualCoelho = (100 / total) * C
percentualRatos = (100 / total) * S
percentualSapos = (100 / total) * R

print(f"RELATORIO FINAL: ")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {percentualCoelho:.2f}")
print(f"Percentual de ratos: {percentualRatos:.2f}")
print(f"Percentual de sapos: {percentualSapos:.2f}")
