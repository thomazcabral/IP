frases = {
    "Oooh look at him": "0",
    "Baseball bat": "1",
    "Aesthetic": "2",
    "Fake Natty": "3",
    "Chris Bumbstead, o CBUM": "4",
    "Pope Francis": "5",
    "O suco vicia": "6",
    "I don't know you tell me": "7",
    "Não é mesmo?": "8",
    "Rodrigo Goes out": "9"
}

quantidade_frases = int(input())
lista_frases = []
lista_numeros = []
m = 0
parar = False
for i in range(quantidade_frases):
    frase = input()
    lista_frases.append(frase)
    if ("+" in frase):
        lista_frases[i] = frase.split("+")

for j in range(len(lista_frases)):
    if type(lista_frases[j]) != list:
        lista_frases[j] = frases[lista_frases[j]]
    else:
        numero = ""
        for k in range(len(lista_frases[j])):
            numero += frases[lista_frases[j][k]]
        lista_frases[j] = numero
lista_frases = [int(num) for num in lista_frases]
lista_frases.sort()
while (len(lista_frases) != 0) and parar == False:
    while m < (len(lista_frases)) and parar == False:
        if lista_frases[m] == 0:
            lista_numeros.append([0])
            lista_frases.remove(lista_frases[m])
            m -= 1
        else:
            x = len(lista_frases)
            for n in range(len(lista_numeros)):
                if lista_numeros[n][-1] + 1 == lista_frases[m]:
                    lista_numeros[n].append(lista_frases[m])
                    lista_frases.remove(lista_frases[m])
                    m -= 1
                    break
            if len(lista_frases) == x:
                parar = True
        m += 1

if (not parar):
    print("YES")
else:
    print("NO")
