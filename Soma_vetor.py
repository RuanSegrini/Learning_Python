n: int
soma: float

soma = 0

n = int(input("Quantos numeros voce vai digitar? "))

vetor: [float] = [0 for x in range(n)]

for i in range(n):
	vetor[i] = float(input("Digite um numero: "))
	soma = vetor[i] + soma
	

media = soma / n

print(f"Valores =",end=" ")
for i in range(n):
    print(f"{vetor[i]}",end=" ")
print(f"\nSOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")