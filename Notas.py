nota1: float
nota2: float
notaFinal: float

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

notaFinal = nota1 + nota2

print(f"NOTA FINAL = {notaFinal:.2f}")

if notaFinal < 60:
    print(f"REPROVADO")
    