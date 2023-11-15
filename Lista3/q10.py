y_voce = int(input())
x_voce = int(input())
y_cambista = int(input())
x_cambista = int(input())
y_pipoca = int(input())
x_pipoca = int(input())
y_barbie = int(input())
x_barbie = int(input())
y_oppenheimer = int(input())
x_oppenheimer = int(input())
pipoca = False
pipoca_pega = False
pipoca_pega_rodada = False
pipoca_roubada = False
x_fixo_pipoca = 0
y_fixo_pipoca = 0
parar = False
tracos = []

for i in range(8):
    tracos.append(["-"] * 8)

tracos[y_voce][x_voce] = "V"
tracos[y_cambista][x_cambista] = "C"
tracos[y_pipoca][x_pipoca] = "P"
tracos[y_barbie][x_barbie] = "B"
tracos[y_oppenheimer][x_oppenheimer] = "O"

while parar == False:
    sentido = input()
    tracos[y_voce][x_voce] = "-"
    tracos[y_cambista][x_cambista] = "-"
    if (x_cambista == x_voce):
        if (y_cambista > y_voce):
            y_cambista -= 1
        elif (y_cambista < y_voce):
            y_cambista += 1
    else:
        if (x_cambista > x_voce):
            x_cambista -= 1
        elif (x_cambista < x_voce):
            x_cambista += 1
    
    if ((x_voce == x_cambista) and (y_voce == y_cambista)):
        parar = True
    if ((x_cambista == x_pipoca) and (y_cambista == y_pipoca)):
        pipoca_roubada = True

    if (not parar):
        if (not pipoca_pega_rodada):
            if (sentido == "cima"):
                y_voce -= 1
            elif (sentido == "baixo"):
                y_voce += 1
            elif (sentido == "direita"):
                x_voce += 1
            elif (sentido == "esquerda"):
                x_voce -= 1
        pipoca_pega_rodada = False
        
        if (((x_voce == x_barbie) and (y_voce == y_barbie)) or ((x_voce == x_oppenheimer) and (y_voce == y_oppenheimer))):
            parar = True
        if ((x_voce == x_cambista) and (y_voce == y_cambista)):
            parar = True

        if (not parar):
            distancia = ((x_voce - x_cambista)**2 + (y_voce - y_cambista)**2)**(1/2)
            if (x_voce == x_pipoca) and (y_voce == y_pipoca) and (pipoca_roubada == False):
                pipoca = True
                pipoca_pega = True
                pipoca_pega_rodada = True
                x_fixo_pipoca = x_pipoca
                y_fixo_pipoca = y_pipoca
                x_pipoca += 100
            
            tracos[y_voce][x_voce] = "V"
            tracos[y_cambista][x_cambista] = "C"

            for linha in tracos:
                print(" ".join(linha))
            
            if (x_voce == x_fixo_pipoca) and (y_voce == y_fixo_pipoca) and (not pipoca_roubada) and (pipoca_pega_rodada):
                print("Finalmente! Peguei a pipoca")
            elif (not pipoca_pega) and (not pipoca):
                print("Ainda não achei a pipoca")
            elif (pipoca) and (pipoca_pega) and (not pipoca_pega_rodada):
                print("Já peguei a pipoca")
            
            if (distancia <= 3):
                print("Preciso acelerar, o cambista tá na minha cola!\n")
            elif (distancia > 4):
                print("O cambista está longe, mas não posso ficar parado\n")
            else:
                print("Consigo ver lá longe o cambista, mas é melhor acelerar!\n")
    if (parar):
        tracos[y_voce][x_voce] = "V"
        tracos[y_cambista][x_cambista] = "C"
        for linha in tracos:
            print(" ".join(linha))
        if (not((x_voce == x_cambista) and (y_voce == y_cambista))) and (not pipoca):
            print("Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.")
        elif ((x_voce == x_barbie) and (y_voce == y_barbie)) and (pipoca):
            print("A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?")
        elif ((x_voce == x_oppenheimer) and (y_voce == y_oppenheimer)) and (pipoca):
            print("Aí sim, que filmaço! Christopher Nolan nunca erra!")
        elif ((x_voce == x_cambista) and (y_voce == y_cambista)):
            print("Droga! Agora volto pra casa sem filme e sem dinheiro.")
