X = int(input(""))
Z = int(input(""))

H = ((34-X)**2 + (220-Z)**2)**(1/2)
print("Distancia para Hogsmeade: ", end="")
print("%.2f" % H)

K = ((0-X)**2 + (0-Z)**2)**(1/2)
print("Distancia para Kakariko: ", end="")
print("%.2f" % K)

S = ((140-X)**2 + (456-Z)**2)**(1/2)

print("Distancia para Solitude: ", end="")
print("%.2f" % S)
