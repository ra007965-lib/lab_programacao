lista = []
for i in range(5):
    nomes = input("Digite os nomes: ")
    lista.append(nomes)
lista2 = lista[ : :-1]
print(f"lista 1: {lista}")
print("\n")
print(f"lista 2: {lista2}")