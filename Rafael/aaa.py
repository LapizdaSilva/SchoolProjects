n = int(input("Digite o valor de numeros primos que deseja gerar: "))

def primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def gerar_primos(n):
    primos = []
    num = 2  # Começa com o primeiro número primo
    while len(primos) < n:
        if primo(num):
            primos.append(num)
        num += 1
    return primos
primos = gerar_primos(n)
print(f"Os primeiros {n} números primos são: {primos}") 