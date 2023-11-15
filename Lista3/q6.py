entrada1 = input().split(" ; ") #objetos no museu, teto de gastos
fim = False
objetos_max = int(entrada1[0])
gastos_max = int(entrada1[1])
objetos = 0
gastos = 0
objeto = []
filmes = []
dinheiro = []
while (fim == False):
    acao = input()
    if (acao == "Quero adicionar um item"):
        caracteristicas = input().split(" - ")
        caracteristicas = [item.split(" , ") for item in caracteristicas]
        if (objetos < objetos_max) and (gastos < gastos_max):
            objetos += 1
            gastos += int(caracteristicas[2])
            objeto.append(caracteristicas[0])
            filmes.append(caracteristicas[1])
            dinheiro.append(caracteristicas[2])
            print(f"Vá em frente, Ken! Você ainda tem {gastos_max - gastos} barbieCoins disponíveis")
        else:
            print("Avise a Barbie que isso não será possível.")
    elif (acao == "Quero remover um item"):
        remover_objeto = input() #verificar índice do objeto e removê-lo junto com o filme de mesmo índice
        if (remover_objeto not in objeto):
            print("Barbie, infelizmente não consegui fazer isso.")
        else:
            objetos -= 1
            index = objeto.index(remover_objeto)
            objeto.remove(remover_objeto)
            filmes.remove(filmes[index])
            gastos -= int(dinheiro[index])
            print(f"Ok, Barbie!\nKen, você ainda tem {gastos} barbieCoins disponíveis")
    elif (acao == "Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?"):
        if (len(objeto) == 0):
            print("Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!")
        else:
            print("Claro!")
            for itens in objeto:
                index = objeto.index(itens)
                print(f"{itens} - {filmes[index]}")
    elif (acao == "Fim! Muito obrigada pela ajuda!!"):
        print("Por nada! Estou sempre à disposição!")
        fim = True
