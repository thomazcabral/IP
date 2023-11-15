esconderijo = input()
local1 = input()

esconderijo = esconderijo.lower()

if (local1.lower() != esconderijo):
    print("Carambolas, ele não está aqui. Ele continua se divertindo!")
    local2 = input()
    if (local2.lower() != esconderijo):
        print("Carambolas, ele não está aqui. Ele continua se divertindo!")
        local3 = input()
        if (local3.lower() != esconderijo):
            print("Carambolas, ele não está aqui. Ele continua se divertindo!")
            print("AAAAAAAH, ele escapou de vez!")
        else:
            print("Ahá, te encontrei e é o fim das suas férias!")
    else:
        print("Ahá, te encontrei e é o fim das suas férias!")
else:
    print("Ahá, te encontrei e é o fim das suas férias!")
