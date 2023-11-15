c1 = input()
c2 = input()
amor = input()
habilidade = input()
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

if (c1 != "Humildade" or c2 != "Bondade"):
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não possui as característica necessárias!")
elif (amor != "Ninguem" and amor != "Mary"):
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não está apaixonado pela pessoa certa!")
elif (habilidade != "Lancar" and habilidade != "Dancar"):
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não possui as habilidades necessárias!")
elif ((nota1 + nota2 + nota3) / 3 < 7):
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não obteve um bom desempenho escolar!")
else:
    print("Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!")
