def funcao(a, b, c, i):
    if a == "Quero somar esses dois números:":
        res = b + c
    elif a == "Preciso subtrair um pelo outro":
        res = b - c
    elif a == "Quanto dá o produto disso?":
        res = b * c
    elif a == "Vou dividir aqui rapidinho":
        res = b / c
    else:
        res = b **c
    print(f"O resultado da {i + 1}ª operação foi {res:.1f}")

numero = int(input())
i = 0

while (i < numero):
    operacao = input()
    n1 = float(input())
    n2 = float(input())
    funcao(operacao, n1, n2, i)
    i += 1

if (i == 0):
    print("Vou relaxar aqui na minha nave")
else:
    print("Ufa, já deu de cálculos por hoje!")
