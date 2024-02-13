distancia1: float
distancia2: float
distancia3: float

print(f"Digite as tres distancias: ")
distancia1 = float(input())
distancia2 = float(input())
distancia3 = float(input())

if distancia1 > distancia2 and distancia1 > distancia3:
    print(f"MAIOR DISTANCIA: {distancia1}")

elif distancia2 > distancia1 and distancia2 > distancia3:
    print(f"MAIOR DISTANCIA: {distancia2}")

else:
    print(f"MAIOR DISTANCIA: {distancia3}")