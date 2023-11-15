duracao_playlist = int(input())
dia = 1
fim_playlist = False
meta = 10
nome_animada = ""
indice_animada = 0
animacao = 0

while (dia < 4 and fim_playlist == False):
    musicas_dia = int(input())
    print(f"Dia {dia} do InterCIn")
    for i in range(musicas_dia):
        nome = input()
        duracao_musica = int(input())
        duracao_playlist -= duracao_musica
        indice = int(input())
        animacao += int(0.8 * indice)
        if (indice > indice_animada):
            indice_animada = indice
            nome_animada = nome

    print(f"A música mais animada do dia foi {nome_animada}")
    
    if (dia == 1 or dia == 2):
        if (meta > animacao):
            meta = 10 + meta - animacao
            print(f"Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {meta} pontos de animação no outro dia")
        else:
            meta = 10
    else:
        if (duracao_playlist > 0):
            if (meta > animacao):
                print("Valeu a tentativa, na próxima vai dar bom")
                print("A playlist estava boa, mas não foi o suficiente para animar o evento")
            else:
                print("A playlist estava incrível demais!")

    if (duracao_playlist <= 0):
        fim_playlist = True
        print("Estava animado, mas a playlist acabou antes do evento terminar e todo mundo ficou muito triste :(")

    dia += 1
    nome_animada = ""
    indice_animada = 0
    animacao = 0
