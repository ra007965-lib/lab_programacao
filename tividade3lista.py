lista1 = [1,2,3,4]
lista2 = [10,20,30,40,50,60]
lista_intercalada = [1,10,2,20,3,30,4,40,50,60]
item_removido0 = lista1.pop(0)
item_removido1 = lista1.pop(0)
item_removido2 = lista1.pop(0)
item_removido3 = lista1.pop(0)
lista3 = (item_removido0, lista2[0],item_removido1,lista2[1],item_removido2,lista2[2],item_removido3,lista2[3],lista2[4],lista2[5])
print(lista3)