def palindromo(entrada_legal):
    tras = []
    for i in range(len(entrada_legal)):
        caractere = entrada_legal[len(entrada_legal) - i - 1].lower()
        tras.append(caractere)
    tras_pra_frente = "".join(tras)
    return tras_pra_frente

def apendar(entrada_legal):
    letras = []
    for i in range(len(entrada_legal)):
        if (entrada_legal[i] not in letras):
            letras.append(entrada_legal[i])
    return len(letras)
        

n = int(input())
for i in range(n):
    entrada = input()
    entrada_legal = entrada.replace(" ", "").lower()
    if (entrada_legal == palindromo(entrada_legal) and entrada.isnumeric()):
        print(f'O número "{entrada}" é um palíndromo!\nHá {apendar(entrada_legal)} número(s) distinto(s) na sequência de números.')
    else:
        if (entrada_legal == palindromo(entrada_legal)):
            print(f'A frase "{entrada}" é um palíndromo!\nHá {apendar(entrada_legal)} letra(s) distinta(s) na frase.')
        else:
            print("A frase ou o número não é um palíndromo.")
