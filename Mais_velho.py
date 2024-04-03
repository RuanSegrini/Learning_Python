n: int
x: int
maior_idade: int

x = 0
maior_idade = 0

nomes = []

n = int(input("Quantos elementos vai ter o vetor? "))

idades: [int] = [0 for x in range(n)]

for i in range(n):
    x += 1
    print(f"Dados da {x}a pessoa: ")
    nome = input(f"Digite um nome: ")
    nomes.append(nome)
    idades = int(input("Idade: "))
    if maior_idade < idades:
     mais_velho = nome
     maior_idade = idades

    
	
    
print(f"PESSOA MAIS VELHA: ",mais_velho)


