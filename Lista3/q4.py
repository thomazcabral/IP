parar = False
iguais = True
i = 0
while (parar == False):
    opcao = input()
    if (opcao == "Explorar arara"):
        profissoes_fora = []
        quantidade = 0
        profissoes = input().split(", ") #lista criada
        barbie_profissoes = input().split(", ")
        print(f"Arara {i}:")
        if (len(profissoes) != len(barbie_profissoes)):
            print("Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!")
        else:
            for profissao in profissoes:
                if profissao not in barbie_profissoes:
                    iguais = False
                    profissoes_fora.append(profissao)
                    quantidade += 1
            if (iguais == True):
                print("Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!")
            else:
                print(f"Poxa, Barbie! Você acabou desorganizando essa arara, e {quantidade} profissões vão ficar de fora da conversa. São elas: {', '.join(profissoes_fora)}.")
        i += 1
    else:
        parar = True
