n: int
x: int
maior_altura: float
menor_altura: float
homem: int
soma: float
contador: int
altura_mulher: float
media: float

altura_mulher= 0
homem = 0
maior_altura = 0
menor_altura = 0
contador = 0
x = 0
contador = 0
media = 0

n = int(input("Quantas pessoas serao digitadas? "))

altura: [float] = [0 for x in range(n)]

for i in range(n):
    x += 1
    altura = float(input("Altura da {}a pessoa: ".format(x)))
    genero = input("Genero da {}a pessa: ".format(x))

    if genero == 'F':
        altura_mulher = altura_mulher + altura
        contador += 1
    else:
        homem += 1

    if maior_altura < altura:
        maior_altura = altura
    if menor_altura > altura or menor_altura == 0 :
        menor_altura = altura

media = altura_mulher / contador


print(f"Menor altura = ", menor_altura)
print(f"Maior altura = ", maior_altura)
print(f"Media das alturas das mulheres = {media:.2f}")
print(f"Numero de homens =", homem) 




   
