minutos_ideal = int(input())
numero = int(input())
posicoes = []
minutos = []
soma = False

for i in range(numero):
    entrada = input().split(" ")
    posicoes.append(entrada[0])
    minutos.append(entrada[1])

for b in range(len(minutos)):
    minutos[b] = int(minutos[b])

for i in range(len(minutos)):
    if (not soma):
        for j in range(i, len(minutos) + 1):
            if sum(minutos[i:(j + 1)]) == minutos_ideal: # verifica se a soma dos j primeiros elementos bate com minutos_ideal
                soma = True
                for k in range(len(minutos)):
                  if k < i:
                    posicoes.remove(posicoes[0]) # após achar a soma, ele retira as posições cujos minutos são inutéis
                  elif k > j:
                    posicoes.remove(posicoes[-1])
                break
if (soma):
    print(f"Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {' '.join(posicoes)}!")
else:
    print("Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima")
