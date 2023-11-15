def pertence(a, b):
    erro = False
    if (len(a) == len(b)):
        i = 0
        while i < len(a):
            if (a[i] == b[i]):
                if (i == len(a) - 1):
                    return True
                else:
                    i += 1
            else:
                break
    else:
        if (len(a) > len(b)):
            return False
        j = 0
        while j < len(a) + 1 and (not erro):
            try:
                if (a[j] == b[j]):
                    j += 1
                else:
                    return pertence(a, b[j + 1:])
            except IndexError:
                erro = True
                return True
    if (len(b) == 0):
        return False


nome = input()
string = input().lower()
nome_minusculo = nome.lower()

if (pertence(nome_minusculo, string)):
    print(f"Encontrei, o culpado é o {nome}!")
else:
    print(f"Não era o {nome}, tenho que continuar procurando.")
