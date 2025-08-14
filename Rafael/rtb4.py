def calv():
    vel = float(input("Qual a sua velocidade em km/h? "))

    multa1 = 0.5
    multa2 = 0.45
    if vel <= 200:
        print('Em viagens de até 200 km o preço da passagem é R$0,50 por km \n o valor q vc tem q pagar é ', multa1 * vel,'R$')
    elif vel > 200:
        print('Em viagens com mais de 200 km o preço da passagem é R$0,45 por km \n o valor q vc tem q pagar é ', multa2 * vel,'R$')

calv()

def calculadora():

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

calculadora()

def calv2():
    val = float(input("Qual o valor da casa que deseja comprar? "))
    sal = float(input("Qual o seu salário? "))
    anos = int(input("Em quantos anos deseja pagar? "))
    
    meses = anos * 12
    prest = val / meses
    val_prest = sal * 0.3
    
    if prest <= val_prest:
        print(f"O empréstimo foi APROVADO, o valor de cada prestação sera: {prest:.2f}")
    else:
        print(f"O empréstimo NÃO foi APROVADO, o valor de {prest:.2f} por mês, \npassou o seu limite de {val_prest:.2f}, por mês")
    
calv2()

def calv3():
    energ = float(input("Quantos kWh voce utilizou este mês? "))
    inst = int(input("Qual o seu tipo de instalação?\n 1- Residencial \n 2- Comercial \n 3- Industrial"))

    R1 = 0.40
    R2 = 0.65

    if inst == 1 and energ <= 500:
        print('O valor da sua energia é:', energ * R1, 'R$')

calv3()