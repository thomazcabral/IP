def add(suspects):
    suspect = input()
    suspects[suspect] = {"Suor": "Seco"}
    print(f"Novo suspeito: {suspect}")
    return suspects


def update(suspects):
    try:
        att = input().split("-> ")
        att[1] = att[1].split(", ")
        for i in range(len(att[1])):
            parts = att[1][i].split(": ")
            suspects[att[0]][parts[0]] = parts[1]
        return suspects
    except:
        print("Quem é esse crazy man? Não tá aqui na database")
        return suspects


def remove(suspects):
    try:
        name = input()
        del suspects[name]
        print(f"{name} removido da lista de suspeitos, está limpo")
        return suspects
    except:
        print("Quem é esse crazy man? Não tá aqui na database")
        return suspects


def judge(suspects, name):
    counter = 0
    try:
        if ("Biceps" in suspects[name] and int(suspects[name]["Biceps"].strip("cm")) > 45):
            counter += 1
        if ("Treino" in suspects[name]):
            number = ""
            time = 0
            train = suspects[name]["Treino"]
            for char in train:
                if (char.isdigit()):
                    number += char
            train = train.strip(" " + number)
            number = int(number)
            if (train == "segundo" or train == "segundos"):
                time = number/60
            elif (train == "minuto" or train == "minutos"):
                time = number
            elif (train == "hora" or train == "horas"):
                time = number*60

            if (time < 30):
                counter += 1
        if ("Frequencia" in suspects[name] and int(suspects[name]["Frequencia"][0]) < 4):
            counter += 1
        if ("BF" in suspects[name] and int(suspects[name]["BF"].strip("%")) < 10):
            counter += 1
        if ("Suor" in suspects[name] and suspects[name]["Suor"] == "Seco"):
            counter += 1
        if (counter >= 3):
            suspects[name]["Condicao"] = "Fake"
            veredict = f"Eu já tenho o meu veredito, e o meu veredito, {name}:\nFAKE NATTY! USOU O SUCO!"
        else:
            suspects[name]["Condicao"]  = "Natural"
            veredict = f"Eu já tenho o meu veredito, e o meu veredito, {name}:\nNatural"
        return suspects, veredict
    except:
        print("Quem é esse crazy man? Não tá aqui na database")
        return suspects, ""


def nattymeter(suspects):
    print("NattyMeter, ON!")
    fake = 0
    natural = 0
    for name in list(suspects.keys()):
        suspects, veredict = judge(suspects, name)
        if (suspects[name]["Condicao"] == "Natural"):
            natural += 1
        else:
            fake += 1
    if (fake == 0):
        print("Oh yeah, vivemos em uma sociedade sem suco, um great day")
    else:
        print(f"NOOO! {int(fake / (fake + natural) * 100)}% USARAM O SUCO")

suspects = {}

while True:
    features = input()
    if (features == "Adicionar suspeito"):
        suspects = add(suspects)
    elif (features == "Atualizar suspeito"):
        suspects = update(suspects)
    elif (features == "Remover suspeito"):
        suspects = remove(suspects)
    elif (features == "Julgamento"):
        name = input()
        suspects, veredict = judge(suspects, name)
        if (veredict != ""):
            print(veredict)
    elif (features == "NattyMeter"):
        nattymeter(suspects)
    else:
        break
