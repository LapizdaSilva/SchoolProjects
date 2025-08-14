def Lista():

    lista = [3,1,2,5,6]

    print('Os números presentes na lista são: ', lista)
    def lista_ordenada(lista):
        return lista

    lt1 = int(input('Digite um número para adicionar a lista: '))
    lista.append(lt1)

    lt2 = int(input('Digite um número para remover da lista: '))
    if lt2 in lista:
        lista.remove(lt2)
    else:
        print('O número não está presente na lista')

    lista.sort()
    print(lista_ordenada(lista))


def Calculadora():

    num1 = int(input('Digite o primeiro Número: '))
    num2 = int(input('Digite o segundo Número: '))
    op = input('Digite o operador (+, - , /, *): ')


    if op == '+':
        print(num1+num2)
    if op == '-':
        print(num1-num2)
    if op == '/':
        print(num1/num2)
    if op == '*':
        print(num1*num2)


def ImparPar():

    num3 = int(input('Digite um Número: '))
    imp = num3 % 2

    if imp > 0:
        print('Impar')
    else:
        print('Par')
        
        
def NumAl():

    import random

    num4 = random.randint(1,10)
    num5 = int(input('Digite um número de 1 a 10: '))

    if num4 == num5:
        print('Você acertou')
    else:
        print('Você errou, o número era: ', num4)
        
        
def Inv():
    pal = input('Digite uma palavra: ')
    pal = pal[::-1]
    print(pal)
    
    
def Fatorial():
    num6 = int(input('Digite um número: '))
    fat = 1 
    for i in range(1, num6+1):
        fat = fat * i
    print(fat)
        
        
def Palindromo():
    pali = input('Digite uma palavra: ')
    if pali == pali[::-1]:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')
        
        
def FizzBuzz():
    for fi in range(1,21):
        if fi % 3 == 0 and fi % 5 == 0:
            print('FizzBuzz')
        elif fi % 3 == 0:
            print('Fizz')
        elif fi % 5 == 0:
            print('Buzz')
        else:
            print(fi)
            
FizzBuzz()


def Menu():
    while True:
        print('\nMenu:')
        print('1 - Lista')
        print('2 - Calculadora')
        print('3 - Impar ou Par')
        print('4 - Número Aleatório')
        print('5 - Palavra Invertida')
        print('6 - Fatorial')
        print('7 - FizzBuzz')
        print('8 - Palíndromo') 
        print('9 - Sair')
        try:
            op = int(input('Digite a opção desejada: '))

            if op == 1:
                Lista()
            elif op == 2:
                Calculadora()
            elif op == 3:
                ImparPar()
            elif op == 4:
                NumAl()
            elif op == 5:
                Inv()
            elif op == 6:
                Fatorial()
            elif op == 7:
                FizzBuzz()
            elif op == 8:
                Palindromo()
            elif op == 9:
                print('Saindo...')
                break
            else:
                print('Opção inválida')
        
        except ValueError:
            print('Digite um número válido')
Menu()