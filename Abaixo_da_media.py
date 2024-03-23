media: float
soma: float
vetSeparado: float

vetLista = []
abaixoMedia = []
vetSeparado = []

media = 0
soma = 0


n = int(input("Quantas pessoas serao digitadas? "))

vetLista: [float] = [0 for x in range(n)]


for i in range(n):
    vett = float(input("Digite um numero: "))
    vetLista.append(vett)
    soma = vett + soma

media = soma / n

print(f"MEDIA VETOR = {media:.3f}")
print(f"ELEMENTOS ABAIXO DA MEDIA: ")

for i in range(n):
    if vetLista[i] < media:
        print(f"{vetLista[i]}")



