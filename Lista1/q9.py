max_vida_venom = int(input())
ataque_venom = int(input())
pocao_venom = int(input())
vida_creeper = int(input())
vida_druida = int(input())
ataque_druida = int(input())
vida_venom = 0
a = 0 # 0 ELE VENCE

#turno 1
print(f"SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O CREEPER!")
ataque_creeper = ataque_venom
vida_venom = max_vida_venom - ataque_creeper
vida_creeper = vida_creeper - ataque_venom
if (vida_venom <= 0 and vida_creeper <=0):
  print("O venom não tankou e foi de base...")
  print("O creeper não tankou e foi de base...")
  print("AH NÃO! O VENOM PEGOU EM BOMBA!")
  a += 1
elif (vida_venom <= 0 or vida_creeper <= 0):
  if (vida_venom <= 0):
    print("O venom não tankou e foi de base...")
    print("AH NÃO! O VENOM PEGOU EM BOMBA!")
    a += 1
  if (vida_creeper <= 0):
    print("O creeper não tankou e foi de base...")
    print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
    if (vida_venom > 0 and vida_venom + pocao_venom <= max_vida_venom):
      vida_venom = vida_venom + pocao_venom
      print("Ah! Essa poção é da boa!")
else:
  print(f"Vida atual do Venom: {vida_venom}")
  print(f"Dano sofrido pelo Venom: {ataque_creeper}")
  print(f"Vida atual do creeper: {vida_creeper}")
  print(f"Dano sofrido pelo creeper: {ataque_venom}")
  if (ataque_venom > ataque_creeper):
    print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
    if (vida_venom > 0 and vida_venom + pocao_venom <= max_vida_venom):
      vida_venom = vida_venom + pocao_venom
      print("Ah! Essa poção é da boa!")
  elif (ataque_creeper > ataque_venom):
    print("AH NÃO! O VENOM PEGOU EM BOMBA!")
    a += 1
  else:
    if (vida_venom > vida_creeper):
      print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
      if (vida_venom > 0 and vida_venom + pocao_venom <= max_vida_venom):
        vida_venom = vida_venom + pocao_venom
        print("Ah! Essa poção é da boa!")
    elif (vida_creeper > vida_venom):
      print("AH NÃO! O VENOM PEGOU EM BOMBA!")
      a += 1
    else:
      print("AH NÃO! O VENOM PEGOU EM BOMBA!")
      a += 1

if (a == 1):
  print("Pelo visto as aventuras do Miles terminaram por aqui...")
else:
#turno 2
  print("SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O DRUIDA!")
  if (vida_venom + pocao_venom <= max_vida_venom):
    vida_venom = vida_venom + pocao_venom
    vida_venom = vida_venom - ataque_druida
    vida_druida = vida_druida - ataque_venom
    ataque_total_druida = ataque_druida
    
  else:
    taxa_envenenamento = abs(vida_venom + pocao_venom - max_vida_venom)
    ataque_total_druida = ataque_druida + taxa_envenenamento
    vida_venom = max_vida_venom - ataque_total_druida
    vida_druida = vida_druida - ataque_venom
  
  ## PARTE DO TURNO 1
  
  if (vida_venom <= 0 and vida_druida <=0):
    print("O venom não tankou e foi de base...")
    print("O druida não tankou e foi de base...")
    print("Pelo visto a poção tava fora do prazo de validade :(")
    a += 1
  elif (vida_venom <= 0 or vida_druida <= 0):
    if (vida_venom <= 0):
      print("O venom não tankou e foi de base...")
      print("Pelo visto a poção tava fora do prazo de validade :(")
      a += 1
    if (vida_druida <= 0):
      print("O druida não tankou e foi de base...")
      print("Quase me dei mal, nunca mais aceito nada de estranho...")
  else:
    print(f"Vida atual do Venom: {vida_venom}")
    print(f"Dano sofrido pelo Venom: {ataque_total_druida}")
    print(f"Vida atual do druida: {vida_druida}")
    print(f"Dano sofrido pelo druida: {ataque_venom}")
    if (ataque_venom > ataque_total_druida):
      print("Quase me dei mal, nunca mais aceito nada de estranho...")
    elif (ataque_total_druida > ataque_venom):
      print("Pelo visto a poção tava fora do prazo de validade :(")
      a += 1
    else:
      if (vida_venom > vida_druida):
        print("Quase me dei mal, nunca mais aceito nada de estranho...")
      elif (vida_druida > vida_venom):
        print("Pelo visto a poção tava fora do prazo de validade :(")
        a += 1
      else:
        print("Pelo visto a poção tava fora do prazo de validade :(")
        a += 1
  if (a == 1):
    print("Pelo visto as aventuras do Miles terminaram por aqui...")

## FIM DOS DOIS TURNOS

if (a == 0):
  print("Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *")
