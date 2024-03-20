n: int
soma: float
nomes = []
idades = []
alturas = []
nomesMenos = []


x = 0
altura = 0
soma = 0
menos = 0


n = int(input("Quantas pessoas serao digitadas? "))


for i in range(n):
	x += 1
	print(f"Dados da {x}a pessoa: ")
	nome = input(f"Digite um nome: ")
	nomes.append(nome)
	idade = int(input("Idade: "))
	idades.append(idade)
	altura = float(input("Alturas: "))
	alturas.append(altura)

	soma = altura + soma

	if idade < 16:
		menos += 1
		nomesMenos.append(nome)

alturaMedia = soma / n
porcentagem = (menos * 100) / n

print(f"Altura media: {alturaMedia:.2f}")
print(f"Pessoas com menos de 16 anos: {porcentagem:.1f}%")
print('\n '.join(map(str,nomesMenos)))
	

