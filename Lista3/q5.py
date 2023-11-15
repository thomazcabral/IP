n = int(input())
lista = []
a = 0
b = n
j = 0
for i in range(n*n):
    y = input()
    lista.append(y)
while j < n:
    print(' '.join(lista[a:b]))
    a += n
    b += n
    j += 1
