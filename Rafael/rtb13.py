'''
Exercício 6.8 Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a
mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída
do while.

Exercício 6.9 Modifique o exemplo para pesquisar dois valores. Em vez de apenas p,
leia outro valor v que também será procurado. Na impressão, indique qual dos
dois valores foi achado primeiro.

Exercício 6.10 Modifique o programa do Exercício 6.9 de forma a pesquisar p e v
em toda a lista e informando o usuário a posição onde p e a posição onde v foram
encontrados.
'''

l = [15, 7, 27, 7, 39]
v = [15, 7, 12, 29, 7]

p = int(input("Digite o primeiro valor a procurar (p): "))
v_valor = int(input("Digite o segundo valor a procurar (v): "))

pos_p = []
pos_v = []

primeira_pos_p = -1
primeira_pos_v = -1

for i in range(len(l)):
    if l[i] == p:
        pos_p.append(i) # coloca a posicao do p na lista pos_p
        if primeira_pos_p == -1: # se for igual a -1 ainda n foi encontrado
            primeira_pos_p = i
    if l[i] == v_valor: # coloca a posicao do v na lista pos_v
        pos_v.append(i)
        if primeira_pos_v == -1: # se for igual a -1 ainda n foi encontrado
            primeira_pos_v = i 

if primeira_pos_p == -1 and primeira_pos_v == -1: # Verifica se os valores n foram encontrados
    print("Nenhum dos dois valores foi encontrado.")
elif primeira_pos_p != -1 and (primeira_pos_v == -1 or primeira_pos_p < primeira_pos_v): # verifica se P foi encontrado
    print(f"{p} foi encontrado primeiro na posição {primeira_pos_p}.") 
elif primeira_pos_v != -1 and (primeira_pos_p == -1 or primeira_pos_v < primeira_pos_p): # verifica se V foi encontrado
    print(f"{v_valor} foi encontrado primeiro na posição {primeira_pos_v}.")

if pos_p:
    print(f"{p} encontrado nas posições: {pos_p}") # se P foi encontrado fala as posicoes
else:
    print(f"{p} não foi encontrado na lista.")

if pos_v:
    print(f"{v_valor} encontrado nas posições: {pos_v}") # se V foi encontrado fala as posicoes
else:
    print(f"{v_valor} não foi encontrado na lista.")