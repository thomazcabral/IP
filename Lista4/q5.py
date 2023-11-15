def funcao_valor(a):
    vogais = ["a", "e", "i", "o", "u"]
    lista = []
    numero = ""
    vogal = 0
    consoantes = 0
    resultado = 0
    for i in a:
      if (i.isnumeric() == True):
        numero += i
      else:
        if (numero != ""):
          lista.append(numero)
        numero = ""
    
    for i in range(len(lista)):
        lista[i] = int(lista[i])
            
    for i in range(1, len(lista)):
        if (lista[i] > lista[0]):
            if (lista[i] % lista[0] != 0): 
                break
            else:
                if (i == (len(lista)) - 1):
                    return 3
    for i in a:
        if (i in vogais):
            vogal += 1
        elif (not i.isdigit()):
            consoantes += 1

    try:
        resultado = int(vogal / consoantes)
    except ZeroDivisionError:
        resultado = 0
    return resultado % 7


x_caracteres = input().lower()
y_caracteres = input().lower()
m = 0

x_valor = funcao_valor(x_caracteres)
y_valor = funcao_valor(y_caracteres)

matriz = []

for j in range(7):
    matriz.append(["."] * 7)

matriz[x_valor][y_valor] = "☆"

for linha in matriz:
    print(" ".join(linha))

if (x_valor == y_valor == 3):
    print("Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!")
    print("Obrigado pela ajuda! A foto ficou ótima!")
elif (x_valor == 0 or y_valor == 0 or x_valor == 6 or y_valor == 6):
    print("Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código...")
    print("Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.")
else:
    print("Ok, agora é só enviar a matriz!")
    print("Obrigado pela ajuda! A foto ficou ótima!")
