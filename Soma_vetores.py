
vetA = []
vetB = []
vetC = []



n = int(input("Quantos numeros voce vai digitar? "))


print(f"Digite os valores do vetor A: ")
for i in range(n):
    vettA = int(input())
    vetA.append(vettA)

print(f"Digite os valores do vetor B: ")
for i in range(n):
    vettB = int(input())
    vetB.append(vettB)


vetC = [sum(pair) for pair in zip(vetA, vetB)]
   
print(f"VETOR RESULTANTE: ")
print('\n'.join(map(str,vetC)))