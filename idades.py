nome: str
nome2: str
idade: int
idade2: int
media: float

print(f"Dados da primeira pessoa: ")
nome = input("Nome: ")
idade = int(input("Idade: "))
print(f"Dados da segunda pessoa: ")
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))

media = (idade + idade2) / 2

print(f"A idade media de {nome} e {nome2} e de {media:.1f} anos")