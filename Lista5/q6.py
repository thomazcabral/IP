def zerar(matriz):
    nova_matriz_i = []
    for j in range(len(matriz)):
        if (matriz[j] == "H" or matriz[j] == "X"):
            nova_matriz_i.append(matriz[j])
        else:
            nova_matriz_i.append("O")
    return "".join(nova_matriz_i)


def cair(matriz):
    linhas, colunas = len(matriz), len(matriz[0])
    nova_matriz = [list(linha) for linha in matriz]  # Cria uma nova matriz baseada na matriz original
    for i in range(linhas - 1, 0, -1):
        for j in range(colunas):
            if nova_matriz[i][j] not in ["X", "H"] and nova_matriz[i - 1][j] in ["X", "H"]:
                nova_matriz[i][j] = nova_matriz[i - 1][j]
                nova_matriz[i - 1][j] = "O"
    return nova_matriz

def executar_caida(matriz):
    while True:
        copia_matriz = [linha[:] for linha in matriz]
        nova_matriz = cair(copia_matriz)
        if nova_matriz == matriz:
            break
        return executar_caida(nova_matriz)
    return matriz


def eliminar_x(ordem_matriz, matriz, n, linhas_eliminadas, substituicao, pontuacao):
    x = "".join(matriz[n - 1])
    o = []
    if (n - 1 >= 0):
        if (x == "X" * ordem_matriz):
            for k in range(ordem_matriz):
                o.append("O")
            matriz.pop(n - 1)
            matriz.insert(n - 1, o)
            pontuacao += ordem_matriz**2 * max(ordem_matriz, linhas_eliminadas)
            linhas_eliminadas += 1
            substituicao = True
            matriz = executar_caida(matriz)
            return eliminar_x(ordem_matriz, matriz, n, linhas_eliminadas, substituicao, pontuacao)
        return eliminar_x(ordem_matriz, matriz, n - 1, linhas_eliminadas, substituicao, pontuacao)
    return matriz, linhas_eliminadas, pontuacao

def coordenada(matriz, coordenadas, ordem_matriz, linhas_eliminadas, substituicao, pontuacao):
    if (int(coordenadas[0]) >= 0 and int(coordenadas[0]) < ordem_matriz and int(coordenadas[1]) >= 0 and int(coordenadas[1]) < ordem_matriz and matriz[int(coordenadas[0])][int(coordenadas[1])] not in ["X", "H"]):
        matriz[int(coordenadas[0])].pop(int(coordenadas[1]))
        matriz[int(coordenadas[0])].insert(int(coordenadas[1]), coordenadas[2])
    matriz = executar_caida(matriz)
    matriz, b, pontuacao = eliminar_x(ordem_matriz, matriz, ordem_matriz, linhas_eliminadas, substituicao, pontuacao)
    matriz = executar_caida(matriz)
    return matriz, b, pontuacao

ordem_matriz = int(input())
matriz = []
parar = False
linhas_eliminadas = 0
substituicao = False
pontuacao = 0

for i in range(ordem_matriz):
    matriz.append(list(input()))

nova_matriz = executar_caida(matriz)

matriz_eliminado, linhas_eliminadas, pontuacao = eliminar_x(ordem_matriz, nova_matriz, ordem_matriz, linhas_eliminadas, substituicao, pontuacao)

matriz_final = matriz_eliminado
b = linhas_eliminadas - 1
while (not parar):
    coordenadas = input().split(",")
    if (coordenadas == ["sair"]):
        parar = True
    else:
        matriz_final, b, pontuacao = coordenada(matriz_final, coordenadas, ordem_matriz, linhas_eliminadas, substituicao, pontuacao)
        linhas_eliminadas = b

for j in range(len(matriz_final)):
    matriz_final[j] = zerar(matriz_final[j])

print(f"Resultado:")
for linha in matriz_final:
    print("".join(linha))
print(f"Pontuação: {pontuacao}")
