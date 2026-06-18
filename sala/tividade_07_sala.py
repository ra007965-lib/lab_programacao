pares = []
impares = []
print("Digite 10 numeros inteiros unicos: ")
while len(pares)+len(impares)<10:
    num = int(input("Numero: "))
    if num in pares or num in impares:
        print("Numero já digitado")
        continue
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
print(f"\n vetor pares: {pares}")
print(f"\n vetor impares: {impares}")