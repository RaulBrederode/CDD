time1 = str(input("Escreva o nome do 1° time: "))
time2 = str(input("Escreva o nome do 2° time: "))
gol1 = int(input("Quantos gols fez o time 1? "))
gol2 = int(input("Quantos gols fez o time 2? "))
if gol1 == gol2:
    print("EMPATE")
elif gol1 > gol2:
    print("{} foi o VENCEDOR com {} gols!".format(time1, gol1))
else:
    print("{} foi o VENCEDOR com {} gols!".format(time2, gol2))
