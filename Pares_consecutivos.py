x:int
resto: int
soma: int

x = int(input("Digite um numero inteiro: "))
resto = x % 2

while x != 0:
    if resto != 0:
    
        soma = (x + 1) + (x + 3) + (x + 5) + (x + 7) + (x + 9)
        print(f"SOMA = {soma}")
    else:
        soma = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)
        print(f"SOMA = {soma}")
        
    x = int(input("Digite um numero inteiro: "))
    resto = x % 2
