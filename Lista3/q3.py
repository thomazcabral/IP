numero = int(input())
indesejados1 = ["colete preto", "coturno"]
indesejados2 = ["vestido com babados", "blusa bufante"]
i = 0

while i < numero:
    parar = False
    colecao = input().split(", ")
    notas = input().split(", ")
    for item in indesejados1:
        if item in colecao and not parar:
            print(f"{item} é uma peça muito gótica, não faz o estilo da Glimmer.")
            parar = True
    for item in indesejados2:
        if item in colecao and not parar:
            print(f"{item} é uma peça muito antiquada, infelizmente essa coleção não vai servir...")
            parar = True
    if (not parar):
        notas_int = []
        for j in notas:
            j = int(j)
            notas_int.append(j)
        if (sum(notas_int) / len(notas_int) < 6):
            print("Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.")
        else:
            print("Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.")
    i += 1
