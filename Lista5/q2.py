def fibonacci(a):
    if (a == 0):
        return 0
    elif (a == 1):
        return 1
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)


def verificacao(numero):
    lista = [0, 1]
    while ((lista[-1]) < numero):
        i = len(lista)
        lista.append(fibonacci(i))
    return lista


numeros = input().split(" ") #total de vidas, total de casas
numeros[0] = int(numeros[0])
numeros[1] = int(numeros[1])

i = 0
while (i < numeros[1]) and (numeros[0] > 0):
    numero_casa = int(input())
    if (numero_casa in verificacao(numero_casa)):
        i += 1
    else:
        print("Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!")
        i = 0
        numeros[0] -= 1
if (numeros[0] > 0):
    print("Voce Adicionou A Master Sword ao seu inventario\nLink Salve Hyrule!!!")
else:
    print("A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf")
