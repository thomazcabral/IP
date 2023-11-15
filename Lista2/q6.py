partidas = int(input())
venceu_jog = False
venceu_adv = False
partidas_jog = 0
partidas_adv = 0

for i in range(partidas):
    if (venceu_adv == False and i != partidas - 1):
        rodadas = int(input())
        print(f"Vai começar a {i + 1}º partida. Esse jogo terá {rodadas} rodada(s).")
        vit_jog = 0
        vit_adv = 0
        for j in range(rodadas):
            hab_jog = int(input())
            hab_adv = int(input())
            if (hab_jog >= hab_adv):
                vit_jog += 1
            else:
                vit_adv += 1
        if (vit_jog > vit_adv):
            venceu_jog = True
            partidas_jog += 1
        else:
            venceu_adv = True
            partidas_adv += 1
        print(f"Fim de jogo! O placar foi {vit_jog}x{vit_adv}")
        
        if (vit_adv >= vit_jog):
            print("Não foi dessa vez! Treinar pro ano que vem!")
        elif (vit_jog - vit_adv >= 5):
            print("QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!")
            venceu_adv = True

        else:
            print("Vamos para próxima fase!")
    
    elif (i == partidas - 1 and venceu_adv == False):
        rodadas = int(input())
        print(f"Tá na hora da grande final! Esse jogo terá {rodadas} rodada(s).")
        vit_jog = 0
        vit_adv = 0
        for j in range(rodadas):
            hab_jog = int(input())
            hab_adv = int(input())
            if (hab_jog >= hab_adv):
                vit_jog += 1
            else:
                vit_adv += 1
        if (vit_jog > vit_adv):
            venceu_jog = True
            partidas_jog += 1
        else:
            venceu_adv = True
            partidas_adv += 1

        print(f"Fim de jogo! O placar foi {vit_jog}x{vit_adv}")
        
        if (partidas_jog > partidas_adv):
            print("É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!")
        else:
            print("Ah não!! Chegaram tão longe mas não foi dessa vez. :(")
