n: int

n = int(input("Deseja a tabuada de qual valor? "))

for i in range(1, 11):
    tabuada =  n * i
    print(f"{n} x {i} = {tabuada}")
