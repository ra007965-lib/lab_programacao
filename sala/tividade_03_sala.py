palavra = input("Digite uma palavra: ").lower
contador_v = 0
for letra in palavra:
    if letra in "aeiou":
        contador_v += 1
print(f"A palavra {palavra} possui {contador_v} vogais")
