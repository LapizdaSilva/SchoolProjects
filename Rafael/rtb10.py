# Exercicio 5.21
valor = float(input(" Digite o valor a pagar: "))
cedula_moeda = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05]
apagar = valor

for atual in cedula_moeda:
    quantidade = int(apagar // atual)
    apagar = round(apagar - (quantidade * atual), 2) 
    if quantidade > 0:
        if atual >= 1: 
            print(f" {quantidade} cédula(s) de R${atual:.2f}")
        else:
            print(f" {quantidade} moeda(s) de R${atual:.2f}")
    if apagar == 0:
        break
    
# Exercicio 5.22
while True:
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '5':
        print("Saindo...")
        break #
    
    numero = int(input("Digite um número para ver a tabuada: "))
    
    if opcao == '1':
        for i in range(1, 11): # Pega um numero de 1 a 10
            print(f"{numero} + {i} = {numero + i}") # vai escrever o numero digitado mais um numero de 1 a 10 ate fechar a tabuada
            #embaixo se repete a mesma coisa e só muda a operação
    elif opcao == '2':
        for i in range(1, 11):
            print(f"{numero} - {i} = {numero - i}")
    elif opcao == '3':
        for i in range(1, 11):
            if i != 0:
                print(f"{numero} / {i} = {numero / i}")
            else:
                print("Não se divide por zero")
    elif opcao == '4':
        for i in range(1, 11):
            print(f"{numero} * {i} = {numero * i}")
    else:
        print("Tente novamente")
        
# Exercicio 5.23
n = int(input("Digite um numero para ver se é primo: "))
def primo(n):
    if n <= 1: # verifica se é menor ou igual a 1
        return False
    if n == 2: #  verifica se é 2
        return True
    if n % 2 == 0: # olha se é par
        return False
    for i in range(3, int(n**0.5) + 1, 2): # verifica os numeros impares até a raiz quadrada do número
        if n % i == 0: # se o resto da divisão for 0, não é primo
            return False
    return True
if primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
    
# Exercicio 5.24
n = int(input("Digite o valor de numeros primos que deseja gerar: "))
def gerar_primos(n):
    primos = []
    num = 2  # Começa com o primeiro número primo
    while len(primos) < n: # enquanto a lista de primos for menor que "n"
        if primo(num):
            primos.append(num) # se for primo, adiciona na lista
        num += 1  # incrementa o número para verificar o próximo
    return primos
primos = gerar_primos(n)
print(f"Os primeiros {n} números primos são: {primos}") 