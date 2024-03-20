n: int
i: int
numeros: float
numero: float
valor: float
posicao: int
maior: float

numeros = []
numero = 0
maior = 0
menor = 0

n = int(input("Quantas pessoas serao digitadas? "))


for i in range(n):
    menor = maior
    numero = float(input("Digite um numero: "))
    numeros.append(numero)
    maior = numero
    if maior >= menor:
        valor = maior
        posicao = i


print(f"MAIOR VALOR = {valor}")
print(f"POSICAO DO MAIOR VALOR = {posicao}")
