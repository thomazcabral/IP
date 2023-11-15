duplas = int(input())
pontvenc = 0
nomevenc = ""
pontperd = 10000
nomeperd = ""

for i in range(duplas):
    nome = input()
    periodo = int(input())
    pontos = int(input())
    pf = pontos / periodo
    if (pf > pontvenc):
        pontvenc = pf
        nomevenc = nome
    if (pf < pontperd):
        pontperd = pf
        nomeperd = nome

print(f"A dupla vencedora foi {nomevenc} com a pontuação final de {pontvenc:.2f} pontos.")
print(f"A dupla perdedora foi {nomeperd} com a pontuação final de {pontperd:.2f} pontos.")
