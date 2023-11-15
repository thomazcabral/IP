e1n1 = input() #equipe 1, nome 1...
e1n2 = input()
e2n1 = input()
e2n2 = input()
partidas = int(input())
pontos1 = 0
pontos2 = 0
vitoria1 = 0
vitoria2 = 0
i = 0
funcionar = True #verificar se o programa deve continuar

print(f"VAMO VER QUEM VAI COMER GRAMA! TEREMOS {partidas} PARTIDAS ENTRE:\n{e1n1} e {e1n2} X {e2n1} e {e2n2}")

while i < partidas and funcionar == True:
    p1 = int(input())
    pontos1 += p1
    p2 = int(input())
    pontos2 += p2
    if (p1 == 0 or p2 == 0):
        if (p1 > p2):
            funcionar = False #parar o programa
            print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")
        else:
            funcionar = False
            print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
    else:
        if (p1 >= p2):
            vitoria1 += 1
        else:
            vitoria2 += 1
    i += 1

while funcionar == True: #verificar se o programa ainda deve continuar
    coeficiente1 = pontos1 * (vitoria1 / partidas)
    coeficiente2 = pontos2 * (vitoria2 / partidas)
    print(f"CARAMBA! Tivemos um total de {pontos1 + pontos2} bolas ao chão ao longo dessa disputa.")
    if (coeficiente1 >= coeficiente2):
        print(f"{e1n1} e {e1n2} são os grandes vencedores!")
        print(f"Mataram {pontos1} bolas, ganhando {vitoria1} partidas")
    else:
        print(f"{e2n1} e {e2n2} são os grandes vencedores!")
        print(f"Mataram {pontos2} bolas, ganhando {vitoria2} partidas")
    funcionar = False #fim definitivo do programa
