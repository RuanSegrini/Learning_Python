idades: int
media: float
quantidade = int
media = 0
quantidade = 0

print(f"Digite as idades: ")
idades = int(input())

if idades < 0:
    print(f"IMPOSSIVEL CALCULAR")

else:
    while idades >= 0:
        media = idades + media
        idades = int(input())
        quantidade = quantidade + 1


    mediareal = media / quantidade
    print(f"MEDIA = {mediareal:.2f}")


