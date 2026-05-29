vetor = []
media = 0
qt_valores = int(input("Quantos valores vão ter na lista: "))

for i in range(qt_valores):
    item = float(input(f"Digite o item {i+1}: "))
    vetor.append(item)
     
for valores in vetor:
    media += valores / qt_valores

valor_aproximado = vetor[0]
menor_distancia = abs(vetor[0] - media)
for valores in vetor:
    valor_atual = abs(valores - media)
    if valor_atual < menor_distancia:
        menor_distancia = valor_atual
        valor_aproximado = valores
        

print(f"Sua lista de valores é: {vetor}")
print(f"A média da lista é: {media}")
print(f"Valor mais proximo da media {valor_aproximado}")