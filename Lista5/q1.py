def fatorial(numero):
    if (numero == 1):
        return 1
    else:
        return (numero * fatorial(numero - 1))


preco = input()
upper = 0
lower = 0
for i in preco:
    if i.isupper():
        upper += 1
    else:
        lower += 1

if (lower > upper):
    num = fatorial(lower) * len(preco)
elif (upper > lower):
    num = fatorial(upper) * len(preco)
else:
    num = (len(preco))**(2)

if (num >= 100):
    print(f"Hum... {num}? Acho que na volta eu compro")
else:
    print(f"{num}! Vou comprar todos!")
