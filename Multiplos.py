x: int
y: int

print(f"Digite dois numeros inteiros: ")

x = int(input())
y = int(input())

if x > y:
    resto = x % y
    if resto != 0:
        print(f"Nao sao multiplos")
    else:
        print(f"Sao multiplos")

else:
    resto = y % x
    if resto != 0:
        print(f"Nao sao multiplos")
    else:
        print(f"Sao multiplos")