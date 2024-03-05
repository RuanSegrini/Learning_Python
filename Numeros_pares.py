n: int
quantidade: int
quantidade = 0

n = int(input("Quantos numeros voce vai digitar? "))

vetor: [int] = [0 for x in range(n)]

for i in range(n):
	vetor[i] = int(input("Digite um numero: "))

print("NUMEROS PARES:")

for i in range(n):
	if vetor[i] % 2 == 0:
		print(f"{vetor[i]}")
		quantidade += 1
		
print(f"QUANTIDADE DE PARES = {quantidade}")