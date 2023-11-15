quantidade = int(input())
dicionario_natty = {}
dicionario_fake = {}
infos = []

for i in range(quantidade):
    entradas = input()
    infos.append(entradas)

for entrada in infos:
    nome, numero, tipo = entrada.split(" - ")
    if (tipo == "natty"):
        dicionario_natty[nome] = (int(numero), entrada)
    else:
        dicionario_fake[nome] = (int(numero), entrada)

ordem_numero_natty = sorted(dicionario_natty.values(), key=lambda x: (-x[0], infos.index(x[1])))
ordem_numero_fake = sorted(dicionario_fake.values(), key=lambda x: (-x[0], infos.index(x[1])))
#key=lambda x ---> fala sobre como os valores devem ser comparados
#-x[0] ---> utilizado para ser sortido na ordem descrescente
#infos.index(x[1]) ---> recupera o índice da entrada mais recente, para caso haja um empate na pontuação

for algo, entrada in ordem_numero_natty:
    print(entrada)

for algo, entrada in ordem_numero_fake:
    print(entrada)
