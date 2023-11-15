frases = []
trigramas = []
dicionario = {}
dict_lists = {}
i = 0
while True:
    frase = input().lower()
    if (frase == "end_of_file"):
        break
    frases.append(frase)

for j in range(len(frases)):
    if (frases[j] not in dicionario.keys()):
        dicionario[frases[j]] = i
    else:
        frases.pop(j)
    i += 1

for sentenca in frases:
    tri = []
    k = 0
    try:
        while True:
            tri.append(sentenca[k] + sentenca[k + 1] + sentenca[k + 2])
            k += 1
    except IndexError:
        trigramas.append(tri)

quantidade_pesquisas = int(input())
for a in range(len(trigramas)):
    dict_lists[a] = trigramas[a]

for l in range(quantidade_pesquisas):
    pesquisa = input().lower()
    parar = False
    possiveis = []
    pesquisa_tri = []
    k = 0
    try:
        while True:
            pesquisa_tri.append(pesquisa[k] + pesquisa[k + 1] + pesquisa[k + 2])
            k += 1
    except IndexError:
        a = 0
    for t in range(len(trigramas)):
        if ((pesquisa[0] + pesquisa[1] + pesquisa[2]) in trigramas[t]):
            possiveis.append(t)
    for b in possiveis:
        if (not parar):
            for c in pesquisa_tri:
                if c not in dict_lists[b]:
                    parar = True
            if (not parar):
                print(b)
                break
        parar = False
