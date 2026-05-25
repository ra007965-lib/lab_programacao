import random
valores_d6 = []
frequencia = []
quantidade = []
contador = 0

for i in range(100):
    numeros = random.randint(1,6)
    valores_d6.append(numeros)
for face in range(1,7):
    quantidade = valores_d6.count(face)
    frequencia.append(quantidade)
    
print(f"{valores_d6}")
print("\n")
print(f"[{frequencia}]")


