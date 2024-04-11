M: int 
N: int 
negativos: int

negativos = 0

N = int(input("Qual a ordem da matriz? ")) 


mat: [[int]] = [[0 for x in range(N)] for x in range(N)] 


for i in range(0, N): 
 for j in range(0, N): 
    mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

    if mat[i][j] < 0:
            negativos += 1
    
print() 


print("DIAGONAL PRINCIPAL:") 
for i in range(0, N): 
 for j in range(0, N):
    if i == j: 
        print(f"{mat[i][j]}  ", end=" ") 
        

print(f"\nQUANTIDADE DE NEGATIVOS = {negativos}")