def percurso(num_salas, salas, sala_inicial, moedas, espada, zelda, agahnim, i, fim):
    porta = 0
    espada_fixo = espada
    if len(salas[sala_inicial]) == 0:
        return False, moedas
    x = salas[sala_inicial].split(" - ")
    for j in range(len(x)):
        if (x[j] == "◇"):
            moedas += 1
        elif (x[j] == "Zelda"):
            zelda = True
        elif (x[j] == "Agahnim"):
            agahnim = True
        elif (x[j] == "espada"):
            espada = True
        else:
            porta = int(x[j])
    num_salas -= 1
    if (zelda and not agahnim) or (zelda and agahnim and espada_fixo):
        return True, moedas
    elif (not zelda and num_salas != 0):
        agahnim = False
        salas[sala_inicial] = []
        return percurso(num_salas, salas, porta, moedas, espada, zelda, agahnim, i, fim)
    else:
        return False, moedas
            

moedas = 0
espada = False
zelda = False
agahnim = False
fim = False
i = 0
num_salas = int(input())
salas = []
for k in range(num_salas):
    salas.append(input())
sala_inicial = int(input())

lista = percurso(num_salas, salas, sala_inicial, moedas, espada, zelda, agahnim, i, fim)
if (lista[0]):
    print(f"A princesa Zelda está a salvo e ainda conseguimos coletar {lista[1]} rupees")
else:
    print(f"Infelizmente a princesa ainda corre perigo, mas temos {lista[1]} rupees para nos ajudar nas buscas")
