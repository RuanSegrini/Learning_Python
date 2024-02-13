glicose: float

glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100:
    print(f"Classificaçao: Normal")
elif glicose <=140:
    print(f"Classificaçao: Elevado")
else:
    print(f"Classificaçao: Diabetes")