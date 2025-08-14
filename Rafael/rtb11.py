print('\n6.2')
lista1 = ['a', 'b', 'c', 'd', 'e'] # cria uma variavel com uma lista
lista2 = ['d', 'e', 'f', 'g', 'h'] # cria outra variavel com uma lista

lista3 = lista1 + lista2 # junta as duas listas 
print("lista 1", lista1)
print("lista 2", lista2)
print("Lista 3, lista + lista2:", lista3)

print("\n-------------------------------------\n")

print('6.3')
listas = set(lista1 + lista2) # junta duas listas e remove oq tiver repetido por causa do set
lista3 = sorted(listas) # organiza a lsita pq o set escreve de forma aleatoria
print("lista 1", lista1)
print("lista 2", lista2)
print("Lista 3, lista + lista2 sem repetidos:", lista3)