dicionario = {}
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numero = int(input())
for i in range(numero):
    palavra = input()
    for letra in alfabeto:
        palavra_alterada = palavra.replace("_", letra)
        if palavra_alterada not in dicionario:
            dicionario[palavra_alterada] = 1
        else:
            dicionario[palavra_alterada] += 1
sorted_dicionario = sorted(dicionario.items(), key=lambda item: (-item[1], item[0]))
#-item[1] sorta tudo primeiro numericamente de cima pra baixo
#item[0] sorta na ordem alfabética, sendo o critério de desempate
primeira_palavra, primeira_contagem = sorted_dicionario[0]
print(primeira_palavra, primeira_contagem)
