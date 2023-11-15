dia_a = int(input(""))
dia_l = int(input(""))
dia_p = int(input(""))
horas = int(input(""))

dia_a = dia_a * horas
dia_l = dia_l * horas
dia_p = dia_p * horas

x = (dia_a + dia_l + (abs(dia_a - dia_l))) / 2

y = (x + dia_p + (abs(x - dia_p))) / 2

print(round(y))
