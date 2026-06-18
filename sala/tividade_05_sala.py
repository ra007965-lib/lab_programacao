lista = []
contador = 0
for i in range(6):
    numeros = int(input("Digite os numeros: "))
    lista.append(numeros)
X = int(input("Digite o numero a buscar: "))
for i in range(len(lista)):
    if lista[i] == X:
        contador += 1
        prim =  lista.index(X)
    else:
        print("Oxente Miserá!, Não tem esse trem na lixta não!")
        
print(lista, contador, prim)