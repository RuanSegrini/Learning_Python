
n:int
menor:int
maior:int

maior = 0
menor = 0


n = int(input("Qual a ordem da matriz? ")) 

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]
maior_elemento: [int] = [0 for x in range(n)]


for i in range(0, n):
    maior = 0
    for j in range(0, n):
       
        mat[i][j] = int(input(f"Elemento [{i}][{j}]: "))
        if mat[i][j] > maior:
            maior = mat[i][j]
            maior_elemento[i] = maior



print(f"MAIOR ELEMENTO DE CADA LINHA: ")
for i in range(n):
    print(f"{maior_elemento[i]}")


