participantes = int(input())
nome_total = ""
final_total = 0

for i in range(participantes):
    nome = input()
    pont = int(input())
    penal = int(input())
    final = pont - penal
    if (final > final_total):
        final_total = final
        nome_total = nome

print(f"O grande vencedor do torneio foi {nome_total} com um total de {final_total} pontos!")
