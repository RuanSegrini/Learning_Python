escala: str


escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if escala == 'F':
    Fah = float(input("Digite a temperatura em Fahrenheit: "))
    Cel = (5/9) * (Fah - 32)
    print(f"Temperatura equivalente em Celsius: {Cel:.2f}")

else:
    Cel = float(input("Digite a temperatura em Celsius: "))
    Fah = (Cel * 9/5) + 32
    print(f"Temperatura equivalente em Fahrenheit: {Fah:.2f}")
