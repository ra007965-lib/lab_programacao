import random
valores_d20 = []
contador = 0
for i in range(50):
    numeros = random.randint(1,20)
    valores_d20.append(numeros)
if valores_d20[i] == 20:
    contador += 1

      
print(valores_d20)