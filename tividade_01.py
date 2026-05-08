
caixa = []
teste = []
for i in range(10):
    caixa.append(int(input("Digite as posições: "))) 
    caixa.append(caixa)
for y in teste:
    if y not in caixa:
        teste.append(y)
print(len(teste))