n: int
a: float
b: float
c: float
media: float

n = int(input("Quantos casos voce vai digitar? "))

for i in range(0, n):
    print(f"Digite tres numeros: ")
    a = float(input())
    b = float(input())
    c = float(input())

    media = ((a * 2) + (b * 3) + (c * 5)) / 10
    print(f"MEDIA = {media:.1f}")