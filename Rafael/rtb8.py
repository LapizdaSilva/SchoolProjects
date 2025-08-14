# Atividade 5.14
def atv1():
    quan = 0
    while True:
        num = int(input("Digite um número inteiro ou 0 para sair: "))
        quan += 1
        soma = num + quan
        if num == 0:
            break
    print("A soma é:", soma)

# Atividade 5.15
def atv2():
    produtos = {
        1 : 0.50,
        2 : 1.00, 
        3 : 4.00,
        4 : 7.00,
        5 : 8.00 
    }
    soma = 0
    while True:
        print ("\nMenu:")
        for i in range(1, 6):
            print(f"{i} = {produtos[i]}")
        prod = int(input("Escolha o produto a ser comprado:"))
        quan = int(input("Digite a quantidade:"))
        if prod in produtos:
            total = produtos[prod] * quan
            soma += total
            print(f"Total: {total:.2f}")
        else:
            print("Código inválido")
        continuar = int(input("Digite 1 para continuar ou 0 para sair: "))
        if continuar == 0:
            print("o Valor total da sua compra é R$",soma)
            break
        
# Menu
def main():
    menu = {
        1 : ("Atividade 5.14", lambda: atv1()),
        2 : ("Atividade 5.15", lambda: atv2()), 
        3 : ("Sair", None)
    }
    while True:
        print("\nMenu:")
        for i in range(1,4):
            print(f"{i} - {menu[i][0]}")
        op = int(input("Escolha uma opção: "))
        if op == 3:
            break
        elif op in menu and menu[op][1] is not None: #Essa parte verifica se a opção existe e se ela n é None
            menu[op][1]() #Essa parte chama a função referente a opção q foi escolhida
        else:
            print("Opção inválida!")
main()