# 5.4

def tb1():
    num = int(input("digite um numero: "))
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)
# 5.5

def tb2():
    contador = 0
    num = 3
    while contador < 10:
        print(num)
        num += 3
        contador += 1
# 5.6

def tb3():
    contador = 1
    for i in range(1, 11):
        resultado = 3 * i
        print(f"3 x {i} = {resultado}")

# 5.7

def tb4():
    inicio = int(input("Digite o valor inicial: "))
    fim = int(input("Digite o valor final: "))
    for i in range(inicio, fim + 1):
        resultado = 3 * i
        print(f"3 x {i} = {resultado}")
        
# 5.8

def tb5():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = 0 
    somas = []
    for _ in range (abs(num2)):
        resultado += num1
        somas.append(num1)
    if num2 < 0:
        resultado = -resultado
        print(f"{num1} + {num2} = {' + '.join(map(str, somas))} = {resultado}")
    else:
        print(f"{num1} + {num2} = -({' + '.join(map(str, somas))}) = {resultado}")


# 5.9

def tb6():
    num1 = int(input("Digite o Dividendo: "))
    num2 = int(input("Digite o Divisor: "))
    
    quociente = 0
    resto = num1
    
    if num2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        subtracoes = []
        while resto >= num2: 
            novo_resto = resto - num2
            quociente += 1
            subtracoes.append(f"{resto} - {num2} = {novo_resto} ({quociente}ª subtração)")
            resto = novo_resto

        if resto < 0:
            resto = num2 + resto
            quociente -= 1
        
        print(f"{num1} / {num2} = {quociente} tendo {resto} sobrando")
        print("Subtrações realizadas:")
        for sub in subtracoes:
            print(sub)

tb1()