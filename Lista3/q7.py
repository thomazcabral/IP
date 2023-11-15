medica = ["Estetoscopio", "Esfigmomanometro", "Jaleco", "Caneta", "Celular"]
informatica = ["Calculadora", "Oculos", "Notebook", "Camisa Social", "Caderno"]
padeira = ["Rolo", "Caneta", "Avental", "Colher de Pau", "Caderno"]
economista = ["Calculadora", "Caneta", "Camisa Social", "Agenda", "Celular"]
personal = ["Halter", "Agenda", "Celular", "Legging", "Corda"]
trabalho = ["Medica", "Assistente de Informatica", "Padeira", "Economista", "Personal Trainer"]
profissoes = [medica, informatica, padeira, economista, personal]

parar = False
profissao_prevista = input()
profissao_dia = input()
index_profissao_prevista = trabalho.index(profissao_prevista)
profissao_p = profissoes[index_profissao_prevista]
bolsa = profissao_p
index_profissao_dia = trabalho.index(profissao_dia)
profissao_d = profissoes[index_profissao_dia]
itens_dia = profissao_d

while (not parar):
    entrada = input()
    if (entrada == "Adicionar"):
        item = input()
        if (item in bolsa):
            print(f"Barbie, você já colocou {item} na bolsa")
        elif (item in itens_dia):
            bolsa.append(item)
            print(f"{item} adicionado à bolsa")
        else:
            print(f"Barbie, {item} não esta na lista de itens de {profissao_dia}")
    elif (entrada == "Retirar"):
        item = input()
        if (item in bolsa):
            if (item not in itens_dia):
                print(f"{item} retirado da bolsa")
                bolsa.remove(item)
            else:
                print(f"Não faca isso Barbie, você precisa de {item} para trabalhar de {profissao_dia}")
        else:
            print("Barbie, como você vai retirar algo que já não esta ai?")
    elif (entrada == "Sair"):
        parar = True

bolsa.sort()
itens_dia.sort()

print(f"Itens na bolsa: {', '.join(bolsa)}")
if (bolsa == itens_dia):
    print("Boa Barbie, foi na correria mas tudo deu certo!")
elif (len(bolsa) < len(itens_dia)):
    for item in itens_dia:
        if (item not in bolsa):
            item_esquecido = item
            print(f"Oh não!! Barbie, você esqueceu de pegar {item_esquecido}!!")
elif (bolsa != itens_dia):
    for item in bolsa:
        if (item not in itens_dia):
            item_errado = item
            print(f"Barbie, você esqueceu de tirar {item_errado}, você não usa ele trabalhando de {profissao_dia}")
