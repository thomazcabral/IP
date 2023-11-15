time_1 = input()
time_2 = input()
v1 = 0
v2 = 0
pont_1 = 0
pont_2 = 0

i = 0
while i < 5:
    pont_1 = int(input())
    pont_2 = int(input())
    if (pont_1 > pont_2):
        print(f"O vencedor da {i+1}ª rodada foi: {time_1}")
        v1 += 1
    else:
        print(f"O vencedor da {i+1}ª rodada foi: {time_2}")
        v2 +=1
    i += 1
    if (v1 == 3 or v2 == 3):
        if (v1 > v2):
            print(f"O time {time_1} ganhou a partida final!")
            i += 10
        else:
            print(f"O time {time_2} ganhou a partida final!")
            i += 10
