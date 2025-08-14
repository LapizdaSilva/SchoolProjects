'''

Exercício 6.5 Altere o Programa 6.7 de forma a poder trabalhar com vários coman-
dos digitados de uma só vez. Atualmente, apenas um comando pode ser inserido
por vez. Altere-o de forma a considerar operação como uma string.

Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos
e, finalmente, a saída do programa.

Exercício 6.6 Modifique o programa para trabalhar com duas filas. Para facilitar
seu trabalho, considere o comando A para atendimento da fila l; e B, para atendi-
mento da fila 2. O mesmo para a chegada de clientes: F para fila l; e G, para fila 2.
'''

# 6.5 e 6.6.

ultimo = 10
fila = list(range(1, ultimo + 1)) # 6.5 - primeira fila com os 10 primeiros numeros
fila2 = list(range(11, ultimo + 11)) # 6.6 - segunda fila pegando com os 10 proximos numeros

while True: 
    print(f"\nExistem {len(fila + fila2)} clientes na fila")
    print(f"Fila1: {fila}")
    print(f"fila2: {fila2}\n")
    print("Digite F para adicionar um cliente ao fim da fila1 e G para o fim da fila2")
    print("A para realizar o atendimento na fila1 e B para a fila2. S para sair")
    operacao = input("Operação (F, G, A, B, ou S): ")
    for comando in operacao: # 6.5 - Lê tudo que for escrito em operacao
        if comando == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else: 
                print("Fila vazia! Ninguém para atender.")
        elif comando == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido da fila 2") # Os comandos So mudam a letra q tem q falar e sao direcionados para a fila correta
            else: 
                print("Fila 2 vazia! Ninguém para atender.")
                
        elif comando == "F":
            print(f"Adicionado cliente {ultimo + 1} ao fim da fila")
            ultimo += 1 
            fila.append(ultimo)
        
        elif comando == "G":
            print(f"Adicionado cliente {ultimo + 11} ao fim da fila 2")
            ultimo += 1 
            fila2.append(ultimo)    
        elif comando == "S":
            exit() # 6.5 - break n funciona pq ta num loop for
        else:
            print("Operação inválida!")
