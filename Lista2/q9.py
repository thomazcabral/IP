aluno = input()
prof = input()
pontos_aluno = 0
pontos_prof = 0
vit_a = 0
vit_p = 0
vencedor = ""
funcionar = True

print(f"E agora, só pela resenha:\nMelhor de 3 entre: {aluno} e {prof}!\nCOMEÇOU!")

while (vit_a < 2 and vit_p < 2): #verificar fim da série
    while (pontos_aluno < 11 and pontos_prof < 11) or funcionar == True: 
        num = int(input())
        if (num % 2 == 0): #divisível por 2
            pontos_prof += 1
        else:
            pontos_aluno += 1
        print(f"{pontos_aluno} - {pontos_prof}")
        if (abs(pontos_aluno - pontos_prof) >= 2) and (pontos_aluno >= 11 or pontos_prof >= 11):
            funcionar = False
        
    if (pontos_aluno > pontos_prof): #fim de jogo
        vit_a += 1
        vencedor = aluno
    else:
        vit_p += 1
        vencedor = prof
        
    pontos_aluno = 0
    pontos_prof = 0
    funcionar = True

    print(f"{vencedor} ganhou esta partida!")
    print(f"Placar: {aluno} [{vit_a}-{vit_p}] {prof}")

print("FIM DA SÉRIE!")
if (vit_a > vit_p): #verificar o vencedor
    print(f"{aluno} ganhou a série! Puro talento!")
else:
    print(f"{prof} ganhou a série! A experiência ganhou!")
