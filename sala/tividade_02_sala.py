numero = int(input("Digite um numero inteiro positivo: "))
produto = 1
for i in range(1, numero+1,2):
    produto *= i
print(f"Produto: {produto}")