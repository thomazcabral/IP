chance = int(input())
input = input()
heroi = ""
local = ""

if (chance > 50):
    heroi = input
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    if (heroi == "Homem-Aranha"):
        print("O amigo da vizinhança nunca me deixa em paz! Será derrotado!")
    elif (heroi == "Capitão América"):
        print("Derrotar o carinha do escudo vai ser moleza!")
    elif (heroi == "Spider Gwen"):
        print("A namoradinha do spidey nunca será capaz de me derrotar!")
    elif (heroi == "Hulk"):
        print("Esse aí só sabe gritar e quebrar tudo, não será páreo para mim!")
    else:
        print(f"Não conheço esse herói {heroi}. Preciso me preparar para essa batalha!")
else:
    local = input
    print("Ufa, finalmente posso tirar minhas férias!")
    if (local == "Maceió"):
        print("Bem que eu tava com saudade de uma boa praia!")
    elif (local == "Pipa"):
        print("As noites em Pipa parecem muito animadas, to dentro!")
    elif (local == "Caruaru"):
        print("Parece um local muito divertido para aproveitar as festas juninas!")
    elif (local == "Bonito"):
        print("Praticar rapel nas cachoeiras vai ser demais!")
    else:
        print(f"Nunca ouvi falar sobre {local}, mas me parece uma boa ideia!")
