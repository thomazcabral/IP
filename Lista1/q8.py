numero = int(input())

if (numero % 2 == 0):
  numero = (numero / 2)**(1/2) + 2
else:
  numero = (numero / 3) + 3

filme1 = input()
filme2 = input()
filme3 = input()
cansaco = 0

if (filme1 == "Coringa" or filme1 == "Batman vs Superman" or filme1 == "O Cavaleiro das Trevas"):
    print("Algo de errado não está certo!")
else:
  if (len(filme1) != numero):
    print("Miles: Tou frio, melhor ir procurar nas fases mais antigas")
    if (len(filme2) != numero):
      print("Gwen: Cadê o velho??? Queria um autógrafo")
      if (len(filme1) != numero and len(filme2) != numero and len(filme3) != numero):
        print("Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...")
        cansaco = 3
        if (filme1 == "Vingadores: Ultimato"):
          cansaco += 1
        if (filme2 == "Vingadores: Ultimato"):
          cansaco += 1
        if (filme3 == "Vingadores: Ultimato"):
          cansaco += 1
      else:
        print("Miles: Achei o easter egg!!!")
        cansaco = 3
        if (filme1 == "Vingadores: Ultimato"):
          cansaco += 1
        if (filme2 == "Vingadores: Ultimato"):
          cansaco += 1
        if (filme3 == "Vingadores: Ultimato"):
          cansaco += 1
        if (len(filme1) == numero or len(filme2) == numero or len(filme3) == numero):
          filmetop = input()
          duracao = int(input())
          if (cansaco >= 2 and duracao >= 135):
            print("Miles: A mimir")
          elif (cansaco >= 2 and 135 > duracao >= 120):
            print("Gwen: Nada que uma xícara de café não resolva!")
          elif (cansaco < 2 or duracao < 120):
            print(f"Peter: {filmetop} é o melhor filme do homem aranha, 10/10")
    else:
      print("Miles: Achei o easter egg!!!")
      cansaco = 2
      if (filme1 == "Vingadores: Ultimato"):
          cansaco += 1
      if (filme2 == "Vingadores: Ultimato"):
          cansaco += 1
      if (len(filme1) == numero or len(filme2) == numero or len(filme3) == numero):
        filmetop = input()
        duracao = int(input())
        if (cansaco >= 2 and duracao >= 135):
          print("Miles: A mimir")
        elif (cansaco >= 2 and 135 > duracao >= 120):
          print("Gwen: Nada que uma xícara de café não resolva!")
        elif (cansaco < 2 or duracao < 120):
          print(f"Peter: {filmetop} é o melhor filme do homem aranha, 10/10")
  else:
    print("Miles: Achei o easter egg!!!")
    cansaco = 1
    if (filme1 == "Vingadores: Ultimato"):
          cansaco += 1
    if (len(filme1) == numero or len(filme2) == numero or len(filme3) == numero):
      filmetop = input()
      duracao = int(input())
      if (cansaco >= 2 and duracao >= 135):
        print("Miles: A mimir")
      elif (cansaco >= 2 and 135 > duracao >= 120):
        print("Gwen: Nada que uma xícara de café não resolva!")
      elif (cansaco < 2 or duracao < 120):
        print(f"Peter: {filmetop} é o melhor filme do homem aranha, 10/10")
