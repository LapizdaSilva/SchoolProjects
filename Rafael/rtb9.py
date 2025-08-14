valor = float(input(" Digite o valor a pagar: "))
cedula_moeda = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05]
apagar = valor

for atual in cedula_moeda:
    quantidade = int(apagar // atual) # // faz a divisão inteira 
    apagar = round(apagar - (quantidade * atual), 2) # Round vai arredondar o valor para 2 casas decimais para melhorar a precisão | 
    #  "quantidade * atual" é o valor q foi pago com o tipo de nota ou moeda | apagar - (quantidade * atual) é o valor q ainda falta pagar
    if quantidade > 0:
        if atual >= 1: # Se o valor for maior ou igual a 1 é uma cédula
            print(f" {quantidade} cédula(s) de R${atual:.2f}")
        else: # Se o valor for menor que 1 é uma moeda
            print(f" {quantidade} moeda(s) de R${atual:.2f}")
    if apagar == 0: # Se o valor a pagar for 0 não precisa mais de cédulas ou moedas
        break
