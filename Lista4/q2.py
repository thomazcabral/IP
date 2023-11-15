def funcao_entrada():
    entrada = input().split(" ")
    for i in range(1, 3):
        entrada[i] = int(entrada[i])
    return entrada #nome[0], quantidade de propulsores[1] e velocidade dos propulsores[2]

def funcao_desclassificacao(entrada):
    if entrada[1] == 0:
        print(f"BUUMM!! Infelizmente, {entrada[0]} está fora da corrida.")
        return True
    return False

def funcao_printar(entrada, vel_inicial, vel_final):
    print(f"--- Participante: {entrada[0]} ---\nQtd de propulsores Final: {entrada[1]}\nVelocidade Inicial: {vel_inicial} km/h\nVelocidade Final: {vel_final} km/h")

parar = False
desclassificado = False
n_desclassificado = 0
n_classificado = 0
acao = ""

while (not parar):
    try:
        entrada = funcao_entrada()
        vel_inicial = entrada[1] * entrada[2]

        while (acao != "Próximo" and acao != "FIM" and not desclassificado):
            acao = input()
            if (acao == "Pit-Stop Espacial"):
                entrada[1] += 1
            elif (acao == "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra."):
                entrada[1] -= 1
            elif (acao == "Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1..."):
                print(f"O {entrada[0]} achou que não descobriríamos, tirem {entrada[0]} imediatamente da pista.")
                desclassificado = True
                n_desclassificado += 1

            if (funcao_desclassificacao(entrada)):
                desclassificado = True
                n_desclassificado += 1

        if (not desclassificado):
            n_classificado += 1
            if (acao == "Próximo"):
                vel_final = entrada[1] * entrada[2]
                funcao_printar(entrada, vel_inicial, vel_final)
            else:
                vel_final = entrada[1] * entrada[2]
                funcao_printar(entrada, vel_inicial, vel_final)
                parar = True
        desclassificado = False
        acao = ""
    except IndexError:
        parar = True

if (n_classificado > 0):
    print(f"Relatório da CIn Pod Race: {n_classificado} participantes terminaram a corrida e {n_desclassificado} foram desclassificados.")
else:
    print(f"NÃO! Esses Droides me pagam, sabotaram minha corrida!")
