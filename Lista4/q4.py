def sobrevivencia(coordenadas, explosao, raio):
    distancia = ((explosao[0] - coordenadas[0])**2 + (explosao[1] - coordenadas[1])**2)**0.5
    if (distancia <= raio):
        return False
    return True


def centro(coordenadas_sobreviventes):
    total_x = sum(coordenadas[0] for coordenadas in coordenadas_sobreviventes)
    total_y = sum(coordenadas[1] for coordenadas in coordenadas_sobreviventes)
    numero_coordenadas_sobreviventes = len(coordenadas_sobreviventes)
    try:
      centro_x = total_x / numero_coordenadas_sobreviventes
      centro_y = total_y / numero_coordenadas_sobreviventes
    except ZeroDivisionError:
        return None

    return [centro_x, centro_y] 


def resgatar_astronautas(capsulas, explosao, raio):
    sobreviventes = 0
    coordenada = []
    capsulas_sobreviventes = []

    for i in range(len(capsulas)):
        sobrevivente_capsula_i = []
        for j in range(len(capsulas[i])):
            if sobrevivencia(capsulas[i][j], explosao, raio):
                sobreviventes += 1
                sobrevivente_capsula_i.append(capsulas[i][j])
        capsulas_sobreviventes.append(sobrevivente_capsula_i)

    for coordenadas_sobreviventes in capsulas_sobreviventes:
        if centro(coordenadas_sobreviventes) != None:
            coordenada.append(centro(coordenadas_sobreviventes))

    return sobreviventes, coordenada


capsulas = eval(input())
explosao = eval(input())
raio = int(input())
output = []

total_sobreviventes, coordenadas_sobreviventes = resgatar_astronautas(capsulas, explosao, raio)

output.append(total_sobreviventes)
output.append(coordenadas_sobreviventes)

print(output)
