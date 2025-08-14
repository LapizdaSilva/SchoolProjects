import time

# 1
alunos = ['GUSTAVO', 'FELIPE', 'LUCAS', 'VINICIUS', 'GABRIEL', 'MARIA', 'VITOR', 'KELVIN', 'RAFAEL', 'GABRIELY', 'CRISTIAN', 'ISABELY', 
          'GABRIEL', 'SAMARA', 'JOAO', 'FERNANDO', 'RAPHAEL', 'NICOLY', 'LUCAS', 'VINICIUS', 'GUSTAVO', 'MATHEUS', 'MAYRELLE', 'ANA']
alunos.sort(reverse=True)
print(alunos)



# 2
alunos = ['GUSTAVO', 'FELIPE', 'LUCAS', 'VINICIUS', 'GABRIEL', 'MARIA', 'VITOR',
           'KELVIN', 'RAFAEL', 'GABRIELY', 'CRISTIAN', 'ISABELY', 'GABRIEL',
           'SAMARA', 'JOAO', 'FERNANDO', 'RAPHAEL', 'NICOLY', 'LUCAS', 'VINICIUS',
           'GUSTAVO', 'MATHEUS', 'MAYRELLE', 'ANA']


def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):
        print(f'Iteração {i+1}: {elemento}')
        for j in range(0, n-i-1):
            if elemento[j] > elemento[j+1]:
                elemento[j], elemento[j+1] = elemento[j+1], elemento[j]
    print(f'Resultado final: {elemento}')
    return elemento


print("Bubble Sort:")
copia_alunos = alunos.copy() 
inicio = time.time()
resultado_bubble = bubble_sort(copia_alunos)
fim = time.time()
print(resultado_bubble)
print(f"Tempo de execução: {fim - inicio:.6f} segundos\n")