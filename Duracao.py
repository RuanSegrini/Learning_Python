duracao: int
segundos: int
minutos: int
horas: int

duracao = int(input("Digite a duracao em segundos: "))

segundos = duracao % 60
minutos = duracao // 60 % 60
horas = duracao // 3600 % 3600

print(f"{horas}:{minutos}:{segundos}")