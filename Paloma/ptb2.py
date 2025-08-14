import random

def contv(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

def atividade1():
    palavr = str(input("Escreva uma palavra: "))
    quant = contv(palavr)
    print(f"{palavr}, tem {quant} vogais")


def main():
    soma = 0  
    while True:  
        numero = int(input("Digite um número: "))  
        if numero == 0:  
            break  
        soma += numero  
    print(f"A soma dos números é: {soma}")

def numg():
    return random.randint(1,100)
    
def jogo():
    resposta = numg()
    tentativas = 0
    numc = 0

    while numc != resposta:
        tentativas += 1
        numc = int(input("Chute um número: "))
        if numc > resposta:
            print(f"Vc errou, é um número menor que {numc}")
        elif numc < resposta:
            print(f"Vc errou, é um número maior que {numc}")
        else:
            print(f"Parabéns vc acertou em {tentativas} tentativas, o número gerado foi {resposta}")

def jogodrag():
    dragão = 200
    jogador = 100
    
    print("Você está em uma batalha contra um dragão")
    print("Escolha entre atacar e defender para derrotar o dragão")
    print("O dragão irá escolher aleatoriamente suas ações")
    print("1 - Atacar")
    print("2 - Defender")
    
    while jogador > 0 and dragão > 0:
        atkdragão = random.randint(1,2)
        acao = int(input('Escolha sua ação: '))
        
        if acao == 1:
            if atkdragão == 1:
                print("Você atacou e o dragão atacou")
                jogador -= 10
                dragão -= 5
            elif atkdragão == 2:
                print("Você atacou e o dragão defendeu")
                jogador -= 5
                dragão -= 0
        elif acao == 2:
            if atkdragão == 1:
                print("Você defendeu e o dragão atacou")
                jogador -= 0
                dragão -= 5
            elif atkdragão == 2:
                print("Você defendeu e o dragão defendeu")
                jogador -= 0
                dragão -= 0
        if jogador <= 0:
            print("Você perdeu")
        elif dragão <= 0:
            print("Você venceu")
        else:
            print(f"Jogador: {jogador} de vida, Dragão: {dragão} de vida")
    
def Menu():
    while True:
        print('\nMenu:')
        print('1 - Atividade 1')
        print('2 - Atividade 2')
        print('3 - Atividade 3')
        print('4 - Atividade 4')
        print('5 - Sair')
        try:
            op = int(input('Digite a opção desejada: '))

            if op == 1:
                atividade1()
            elif op == 2:
                main()
            elif op == 3:
                jogo()
            elif op == 4:
                jogodrag()
            elif op == 5:
                print('Saindo...')
                break
        except ValueError:
            print('Digite um número válido')

Menu()
