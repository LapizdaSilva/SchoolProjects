# Exercicio 5.11
def tb1():
    di = int(input("Digite o depósito inicial: "))
    ti = float(input("Digite a taxa de juros: "))
    print("Mês\tValor")
    for i in range(1, 25):
        di = di + (di * ti / 100) # Soma o deposito inicial com o juros
        print(f"{i}\t{di:.2f}") #  Escreve o mês e os valores do deposito
    print(f"Total ganho com juros: R${di:.2f}")

# Exercicio 5.12
def tb2():
    di = int(input("Digite o depósito inicial: ")) 
    ti = float(input("Digite a taxa de juros: ")) 
    dm = int(input("Digite o valor depositado mensalmente: ")) 
    print("Mês\tValor")
    for i in range(1, 25):
        di = di + (di * ti / 100) + dm # Soma o deposito inicial com o juros e o deposito mensal
        print(f"{i}\t{di:.2f}")
    print(f"Total ganho com juros: R${di:.2f}")

# Exercicio 5.13
def tb3():
    div_in = int(input("Digite o valor inicial da dívida: ")) 
    jm = float(input("Digite o juro mensal: "))
    vm = int(input("Digite o valor mensal que será pago: "))
    meses = 0
    total = 0
    total_jur = 0
    print("Mês\tValor")
    while div_in > 0:
        div_in = div_in + (div_in * jm / 100) - vm # Soma o valor da dívida com o juros e subtrai o valor mensal
        total += vm # Soma o valor mensal pago
        total_jur += (div_in * jm / 100) # Soma o juros pago
        meses += 1 # Adiciona mais um a variavel mes
        print(f"{meses}\t{div_in:.2f}")
    print(f"Total pago: R${total:.2f}")
    print(f"Total de juros pago: R${total_jur:.2f}")
    print(f"Total de meses: {meses}")
 