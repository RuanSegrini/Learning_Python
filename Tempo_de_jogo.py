inicial: int
final: int
horas: int

inicial = int(input("Hora inicial: "))
final = int(input("Hora final: "))

if inicial > final:
    horas = (24 - inicial) + final
    print(f"O JOGO DUROU {horas} HORA(S)")

elif final > inicial:
    horas = final - inicial
    print(f"O JOGO DUROU {horas} HORA(S)")

else:
    print(f"O JOGO DUROU 14 HORA(S)")