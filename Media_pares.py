n: int
numeros: int
media_pares: float

numeros = 0
contador = 0


n = int(input("Quantos elementos vai ter o vetor? "))

vetor: [int] = [0 for x in range(n)]
vetor_impares = []
for i in range(n):
	vetor[i] = int(input("Digite um numero: "))
	if vetor[i] % 2 == 0:
		numeros = numeros + vetor[i]
		contador += 1


if numeros == 0:
	print(f"NENHUM NUMERO PAR")
else:
    media_pares = numeros / contador
	
    print(f"MEDIA DOS PARES: {media_pares:.1f}")
