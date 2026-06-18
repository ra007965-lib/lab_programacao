dado = 1
while dado != 0:
    dado = int(input("Digite um numero entre 10 e 50: "))
    if dado < 10 or dado > 50:
        print("Dado invalido")
    elif dado >= 10 or dado <= 50:
        print("Dado Valido")
        