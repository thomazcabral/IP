numero = int(input())
criaturas = []

for i in range(numero):
    nome_criatura = input()
    if (nome_criatura in criaturas):
        print("Criatura repetida")
    else:
        criaturas.append(nome_criatura)

print("Registradas:")
for nome in criaturas:
    print(nome)
