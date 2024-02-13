salario: float

salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000:
    novo = ((20 / 100) * salario) + salario
    aumento = ((20 / 100) * salario)

    print(f"Novo salario: R${novo:.2f}")
    print(f"Aumento = R${aumento:.2f}")
    print(f"Porcentagem 20 %")

elif salario <= 3000:
    novo = ((15 / 100) * salario) + salario
    aumento = ((15 / 100) * salario)

    print(f"Novo salario: R${novo:.2f}")
    print(f"Aumento = R${aumento:.2f}")
    print(f"Porcentagem 15 %")

elif salario <= 8000:
    novo = ((10 / 100) * salario) + salario
    aumento = ((10 / 100) * salario)

    print(f"Novo salario: R${novo:.2f}")
    print(f"Aumento = R${aumento:.2f}")
    print(f"Porcentagem 10 %")

else:
    novo = ((5 / 100) * salario) + salario
    aumento = ((5 / 100) * salario)

    print(f"Novo salario: R${novo:.2f}")
    print(f"Aumento = R${aumento:.2f}")
    print(f"Porcentagem 20 %")