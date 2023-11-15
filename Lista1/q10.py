nome_aranha = input()
ataque_aranha = int(input())
defesa_aranha = int(input())
nome_aliado = input()
ataque_aliado = int(input())
defesa_aliado = int(input())
nome_vilao = input()
ataque_vilao = int(input())
defesa_vilao = int(input())
nome_capanga = input()
ataque_capanga = int(input())
defesa_capanga = int(input())
fator_sorte1 = int(input())
fator_sorte2 = int(input())
fator_sorte3 = int(input())
derrotas = 0

# CONFRONTO 1: ARANHA ATACA 
print("1° confronto:")

if (fator_sorte1 == 0):
  if (ataque_aranha >= defesa_vilao):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1
elif (fator_sorte1 == 1):
  if (ataque_aranha + ataque_aliado >= defesa_vilao):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1
elif (fator_sorte1 == 2):
  if (ataque_aranha > defesa_vilao + defesa_capanga):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1
elif (fator_sorte1 == 3):
  if (ataque_aranha + ataque_aliado >= defesa_vilao + defesa_capanga):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1
    
# CONFRONTO 2: VILÃO ATACA
print("2° confronto:")

if (fator_sorte2 == 0):
  if (ataque_vilao > defesa_aranha):
    print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")
    derrotas += 1
  else:
    print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
elif (fator_sorte2 == 1):
  if (ataque_vilao + ataque_capanga >= defesa_aranha):
    print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")
    derrotas += 1
  else:
    print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
elif (fator_sorte2 == 2):
  if (ataque_vilao > defesa_aranha + defesa_aliado):
    print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")
    derrotas += 1
  else:
    print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
elif (fator_sorte2 == 3):
  if (ataque_vilao + ataque_capanga > defesa_aranha + defesa_aliado):
    print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")
    derrotas += 1
  else:
    print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
    
# CONFRONTO 3: ARANHA ATACA
print("3° confronto:")

if (fator_sorte3 == 0):
  if (ataque_aranha >= defesa_vilao):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1
elif (fator_sorte3 == 1):
  if (ataque_aranha + ataque_aliado >= defesa_vilao):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1
elif (fator_sorte3 == 2):
  if (ataque_aranha > defesa_vilao + defesa_capanga):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1
elif (fator_sorte3 == 3):
  if (ataque_aranha + ataque_aliado >= defesa_vilao + defesa_capanga):
    print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
  else:
    print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
    derrotas += 1

## FIM DOS CONFRONTOS

if (derrotas <= 1):
  print(f"O {nome_aranha} e {nome_aliado} conseguiram derrotar o {nome_vilao} e recuperar o multiverso!")
else:
  print(f"O {nome_vilao} e {nome_capanga} invadiram Nova York, onde estão os outros aranhas??")
