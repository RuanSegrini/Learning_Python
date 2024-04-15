m: int; n: int


m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

matriz: [[int]] = [[0 for x in range(n)] for x in range(m)]
negativos: [[int]] = [[0 for x in range(n)] for x in range(m)]

for i in range(m):
	for j in range(n):
		matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))


print("VALORES NEGATIVOS: ")

for i in range(m):
    for j in range(n):
        if matriz[i][j] < 0:
            negativos[i][j] = matriz[i][j]
            print(f"{negativos[i][j]}")