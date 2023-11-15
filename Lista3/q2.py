itens_desejados = input().split(", ")
desejos = []
for i in itens_desejados:
    desejos.append(i)

itens_possuidos = input().split(", ")
possui = []
for j in itens_possuidos:
    possui.append(j)

printar_ordem = [a for a in desejos if a in possui]

if (len(printar_ordem) == 0):
    print(f"Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {len(desejos)} itens em casa.")
else:
    print("Esses são os itens que já tenho em casa:")
    for b in range(len(printar_ordem)):
        print(f"{b + 1}º item: {printar_ordem[b]}")

if (len(printar_ordem) != 0):
    if (len(printar_ordem) == len(desejos)):
        print(f"Que ótimo, consegui encontrar cada um dos {len(desejos)} itens!")
    else:
        print(f"Irei precisar comprar {len(desejos) - len(printar_ordem)} itens antes do meu encontro!")

print("Isso é tudo! Hora de me preparar!")
