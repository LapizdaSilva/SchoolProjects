L = [1, 7, 2, 4]
maximo = L[0]

for e in L: 
    if e < maximo:
        maximo = e

print(maximo)

print("\n---------------------------------------------------")

T = [ -8, 0, 1, 2, 5, -2, -4, -10]
num = T[0]
num2 = T[0]

for i in T:
    if i < num:
        num = i 

for i in T:
    if i > num2:
        num2 = i
        
print(f'\na menor temperatura é: {num}, e a menor é: {num2}, a média é de: {sum(T)/8} ') # imprime a soma da lista divido por oito, fazendo a média