def contv(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in palavra:
        if letra in vogais:
            contador += 1
       
    return(contador)

palavr = str(input("Escreva uma palavra: "))
quant = contv(palavr)
print(f"{palavr}, tem {quant} de vogais")