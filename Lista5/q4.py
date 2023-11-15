def formatacao(coeficientes):
    for i in range(len(coeficientes)):
        if (coeficientes[i] != 0):
            x = coeficientes[i]
            try:
                if (coeficientes[i] == -1 and i != 0 and sum(coeficientes[:i]) != 0):
                    x = "-"
                if (coeficientes[i] == 1 and i != 0 and sum(coeficientes[:i]) != 0):
                    x = "+"
                if (i != 0 and i != 1 and x != "+" and x != "-" and sum(coeficientes[:i]) != 0):
                    if (coeficientes[i] > 0):
                        y = f"+{x}x^{i}"
                    else:
                        y = f"{x}x^{i}"
                elif (i != 0 and i != 1 and (x == "+" or x == "-")) or (i!= 0 and i!= 1 and sum(coeficientes[:i]) == 0):
                    if (coeficientes[i] > 0 and x != 1 and x != -1):
                        y = f"{x}x^{i}"
                    elif (coeficientes[i] < 0 and x != 1 and x != -1):
                        y = f"{x}x^{i}"
                    elif (coeficientes[i] > 0 and x == 1):
                        y = f"x^{i}"
                    elif (coeficientes[i] > 0 and x == -1):
                        y = f"-x^{i}"
                elif (i == 1 and x != "+" and x != "-"):
                    if(coeficientes[i] > 0 and sum(coeficientes[:i]) != 0):
                        y = f"+{x}x"
                    elif (coeficientes[i] < 0 and sum(coeficientes[:i]) != 0):
                        y = f"{x}x"
                    elif (coeficientes[i] > 0 and sum(coeficientes[:i]) == 0):
                        y = f"{x}x"
                    elif (coeficientes[i] < 0 and sum(coeficientes[:i]) == 0):
                        y = f"{x}x"
                else:
                    y = x
            except TypeError:
                if (coeficientes[i] == -1 and i != 0):
                    x = "-"
                if (coeficientes[i] == 1 and i != 0):
                    x = "+"
                if (i != 0 and i != 1 and x != "+" and x != "-"):
                    if (coeficientes[i] > 0):
                        y = f"+{x}x^{i}"
                    else:
                        y = f"{x}x^{i}"
                elif (i != 0 and i != 1 and (x == "+" or x == "-")) or (i!= 0 and i!= 1 and sum(coeficientes[:i]) == 0):
                    if (coeficientes[i] > 0 and x != 1 and x != -1):
                        y = f"{x}x^{i}"
                    elif (coeficientes[i] < 0 and x != 1 and x != -1):
                        y = f"{x}x^{i}"
                    elif (coeficientes[i] > 0 and x == 1):
                        y = f"x^{i}"
                    elif (coeficientes[i] > 0 and x == -1):
                        y = f"-x^{i}"
                elif (i == 1 and x != "+" and x != "-"):
                    if(coeficientes[i] > 0):
                        y = f"+{x}x"
                    elif (coeficientes[i] < 0):
                        y = f"{x}x"
                    elif (coeficientes[i] > 0 and sum(coeficientes[:i]) == 0):
                        y = f"{x}x"
                    elif (coeficientes[i] < 0 and sum(coeficientes[:i]) == 0):
                        y = f"{x}x"
                else:
                    y = x
            coeficientes[i] = str(coeficientes[i]).replace(str(coeficientes[i]), str(y))
            for i in range(len(coeficientes)):
                try:
                    coeficientes[i] = int(coeficientes[i])
                except ValueError:
                    continue
    zero = 0
    j = 0
    while j < len(coeficientes):
        if (coeficientes[j] == 0):
            zero += 1
            coeficientes.remove(coeficientes[j])
            j -= 1
        j += 1
    if (j == 0):
        return 0
    for i in range(len(coeficientes)):
        coeficientes[i] = str(coeficientes[i])
    return ''.join(coeficientes)


def derivada(numeros, ordem_derivada):
    if (ordem_derivada == 0):
        return numeros
    for i in range(len(numeros)):
        numeros[i] = numeros[i] * i
    try:
        numeros.pop(0)
    except IndexError:
        return [0]
    ordem_derivada -= 1
    if (ordem_derivada == 0):
        return numeros
    return(derivada(numeros, ordem_derivada))


grau_polinomio = int(input())
ordem_derivada = int(input())
nao_nulos = int(input())
coeficientes = []

for i in range(grau_polinomio + 1):
    coeficientes.append(0)
for j in range(nao_nulos):
    entrada = input().split(":") #coeficiente 0: 10
    x = int(entrada[0].split()[-1]) #indice
    y = entrada[1].split()[-1] #coeficiente
    coeficientes[x] = int(str(coeficientes[x]).replace("0", y))

numeros = coeficientes.copy()
polinomio = formatacao(coeficientes)
print(f"A derivada {ordem_derivada} do polinômio {polinomio} é\n{formatacao(derivada(numeros, ordem_derivada))}")
