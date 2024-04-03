n: int
x: int
media: float

x = 0


nomes = []
aprovados = []

n = int(input("Quantos elementos vai ter o vetor? "))

nota1: [float] = [0 for x in range(n)]
nota2: [float] = [0 for x in range(n)]

for i in range(n):
    x += 1
    print(f"Digite nome, primeira e segunda nota do {x}o aluno:  ")
    nome = input()
    nomes.append(nome)
    nota1 = float(input())
    nota2 = float(input())

    media = (nota1 + nota2) / 2

    if media >= 6 :
     aprovados.append(nome)
     


print(f"ALUNOS APROVADOS:")    
print('\n'.join(map(str,aprovados)))