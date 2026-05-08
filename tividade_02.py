
caixa = []
posicao = -1
x = int(input("Digite a posição desejada: "))
for i in range(5):
    caixa.append(int(input("Digite as posições: "))) 
    
for i in range(5):
    if caixa[i] == x:
        posicao = i
        break
print(f"Posição = {posicao}")