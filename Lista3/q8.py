parar = False

penteados = input().split(" - ")
tops = input().split(" - ")
bottoms = input().split(" - ")
sapatos = input().split(" - ")
lista = [penteados, tops, bottoms, sapatos]
inicio = []
escolhido = []
roupas_escolhidas = []

print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")
while (parar == False):
    escolhido = []
    roupas_escolhidas = []
    direcao = input().split(" ")
    print("Iniciando mesclagem...")
    for i in range(4):
        inicio.append(int((len(lista[i])/2)))
        if ("<" in direcao[i]):
            escolhido.append(inicio[i] - int(direcao[i].strip("<")))
            while (escolhido[i] < 0 or escolhido[i] >= len(lista[i])):
                if (escolhido[i] < 0):
                    escolhido[i] += len(lista[i])
                else:
                    escolhido[i] -= len(lista[i])
        else:
            escolhido.append(inicio[i] + int(direcao[i].strip(">")))
            while (escolhido[i] < 0 or escolhido[i] >= len(lista[i])):
                if (escolhido[i] < 0):
                    escolhido[i] += len(lista[i]) 
                else:
                    escolhido[i] -= len(lista[i]) 
        roupas_escolhidas.append(lista[i][escolhido[i]])
        inicio[i] = escolhido[i]
    print(f"O look gerado foi:\ncabelo {roupas_escolhidas[0]}, {roupas_escolhidas[1]} com {roupas_escolhidas[2]} e {roupas_escolhidas[3]} nos pés.")
    entrada = input()
    if (entrada != "Acho que não combinou muito :/"):
        parar = True
if (entrada == "Amei!!"):
    if (roupas_escolhidas[1] == "camisa da seleção"):
        print("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
    else:
        print("Essa Barbie vai arrasar com o look perfeito!")
else:
    print("Acho que estou precisando de ajustes, Ken :(")
