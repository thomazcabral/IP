def n_perfeito(numero):
  divisores = []
  for i in range(1, numero):
    if numero % i == 0:
      divisores.append(i)
  if sum(divisores) == numero:
    return True
  else:
    return False

    
a = 1
palavra = []
parada = False
while parada == False:
  binary = ''
  stop = False
  x = 0
  while stop == False:
    string = input()
    if string == 'Todas as expressoes foram enviadas!':
      print(f'A decodificacao final resultou em:\n{"".join(palavra)}')
      stop = True
      parada = True
    elif string == '':
      stop = True
    else:
      desempilhado_exp = ''
      expressao = ''
      string = string.split(' ')
      para = False
      pilha = []
      while para == False:
        for i in range(len(string)):
          if string[i].isnumeric() == True:
            pilha.append(string[i])
          else:
            break
        if len(pilha) <= 2:
          expressao = (f"({f' {string[i]} '.join(pilha)})")
          string.remove(string[i])
          for j in pilha:
            if j in string:
              string.remove(j)
            pilha = []
            pilha.insert(0, expressao)
        else:
          while pilha[0] == expressao:
            desempilhado_exp = pilha.pop(0)
          desempilhado = pilha.pop(0)
          pilha.append(desempilhado)
          if desempilhado_exp != '':
            pilha.append(desempilhado_exp)
          for j in pilha:
            if j in string:
              string.remove(j)
          operacoes = []
          for k in string:
            if k.isnumeric() == False:
              operacoes.append(k)
            else:
              break
          for l in range(len(operacoes)):
            if operacoes[l] == '/':
              if eval(pilha[0]) < eval(pilha[1]):
                eva = pilha.pop(0)
                pilha.append(eva)
            expressao = (f"({f' {operacoes[l]} '.join(pilha[0:2])})")
            if len(pilha) >= 2:
              for i in range(2):
                pilha.pop(0)
            pilha.insert(0, expressao)
            string.remove(operacoes[l])
        if len(string) == 0:
          para = True
      valor = abs(int(eval(expressao)))
      if n_perfeito(valor) == False or valor == 0:
        binary += '0'
      else:
        binary += '1'
  if len(binary) == 8:
    for b in range(len(binary)):
      x += int(binary[b]) * 2**(len(binary) - 1 - b)
    print(f'O {a}º conjunto de expressoes resultou no binario {binary} que em ASCII eh: {chr(x)}\n')
    palavra.append(chr(x))
  a+=1
