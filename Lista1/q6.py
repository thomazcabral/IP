nome = input()
pessoas = int(input())
coeficiente = float(input())
decimal = 0

if (pessoas % 2 == 0):
    fumantes = coeficiente * (pessoas - 1) + 1
else:
    fumantes = (coeficiente * (pessoas - 1) / 2)

if (type(fumantes) != int):
    decimal1 = abs(fumantes - int(fumantes))
    if (decimal1 > 0.5):
        fumantes = int(fumantes) + 1
    else:
        fumantes = int(fumantes)

proporcao = int(fumantes * 100 / pessoas)

print(f"Vamos verificar se {nome} vai fumar singaro!")
print(f"{proporcao}% dos seus amigos fumam singaro")

if (proporcao < 25):
    print("Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde")
elif (proporcao > 50):
    print("TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!")
elif (50 > proporcao > 25):
    print("Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde")
