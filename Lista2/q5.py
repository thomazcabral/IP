jogos = int(input())
manchester = 0
girls = 0
m_jogo = 0
g_jogo = 0
i = 0
funciona =  True

while i < jogos and funciona == True:
    time = input()
    gols = int(input())
    chutes = int(input())
    amarelo = int(input())
    vermelho = int(input())
    if (time == "Manchester CIn"):
        m_jogo += gols*10
        m_jogo += chutes*3
        m_jogo -= amarelo*2
        m_jogo -= vermelho*4
        if (gols >= 0.3*chutes):
            m_jogo += 3
        if (vermelho >= amarelo):
            m_jogo -= 3
    elif (time == "SpiCIn Girls"):
        g_jogo += gols*10
        g_jogo += chutes*3
        g_jogo -= amarelo*2
        g_jogo -= vermelho*4
        if (gols >= 0.3*chutes):
            g_jogo += 3
        if (vermelho >= amarelo):
            g_jogo -= 3
    if (m_jogo < 0):
        funciona = False
        manchester = -1
    if (g_jogo < 0):
      funciona = False
      girls = -1
      
    else:
        manchester += m_jogo
        girls += g_jogo
        m_jogo = 0
        g_jogo = 0
        i += 1
    
if (manchester < 0):
  print("O time Manchester CIn ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
elif (girls < 0):
  print("O time SpiCIn Girls ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
else:
  if (manchester > girls):
    print(f"Com {(manchester / (manchester + girls)):0.2%} dos pontos, o time Manchester CIn pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")
  else:
    print(f"Com {(girls / (manchester + girls)):0.2%} dos pontos, o time SpiCIn Girls pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")
