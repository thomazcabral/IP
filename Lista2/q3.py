garrafas = 20
cin = True
solicitadas = 0

while garrafas > 0 and cin == True:
    frase = input()
    if (frase == "Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores"):
        jog_sede = int(input())
        if (jog_sede > garrafas):
            print(f"Não teremos água para todos os jogadores... Temos que garantir {jog_sede - garrafas} garrafas!!") # talvez retirar garrafas
            garrafas = 2*garrafas - jog_sede
        else:
            garrafas -= jog_sede
    elif (frase == "Encham o cooler, vai começar um jogo!!!!"):
        garrafas += 15
        print("Geladeira cheia!")
    elif (frase == "Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário"):
        for i in range(5):
            numero = int(input())
            solicitadas += numero
        if (solicitadas > garrafas):
            print(F"Prometemos distribuir {solicitadas - garrafas} garrafas e zeramos")
            garrafas -= solicitadas
        else:
            garrafas -= solicitadas
        if (garrafas <= 0):
          print("Por questões logísticas, teremos que acabar com os jogos...")
    elif (frase == "O InterCIn acabou!!! Vamos ver nosso estoque de bebidas"):
        cin = False

if (garrafas > 0):
    print(f"Notícia boa: sobraram {garrafas} garrafas, vamos guardar na geladeira :D")
elif (garrafas < 0):
    print(f"Estamos devendo {abs(garrafas)} garrafas para os alunos...")
else:
    print("Vendemos todas as águas, fizemos uma contagem certeira!!")
