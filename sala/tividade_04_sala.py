lista = []
for i in range(5):
    notas = float(input("Digite o valor das notas: "))
    lista.append(notas)
lista.sort()
lista.pop(0)
print(lista)