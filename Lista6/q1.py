quantidade = int(input())
dicionario = {}
infos = []
for i in range(quantidade):
    entradas = input()
    infos.append(entradas)

mes_desejado = int(input())

for entrada in infos:
    entrada_alterada = entrada.split(" - ")
    nome = entrada_alterada[0]
    segunda_parte = entrada_alterada[1]
    entrada_alteraada = segunda_parte.split()
    profissao = entrada_alteraada[0]
    condicao = entrada_alteraada[1]
    mes = int(entrada_alteraada[2])
    if (mes == mes_desejado) and (condicao == "fake"):
        dicionario.update({nome: profissao})
    elif (condicao == "natural") and (nome in dicionario.keys()):
        del dicionario[nome]
ordem_nome = sorted(dicionario.keys())

if (len(ordem_nome) != 0):
    print("Os fake nattys do mês são:")
    for nome in ordem_nome:
        profissao = dicionario[nome]
        print(f"{nome} - {profissao}")
else:
    print("Até agora não temos ninguém pra expor na internet neste mês :(")
