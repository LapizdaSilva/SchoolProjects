import random

def escolhe():
    lista_palavras = [
        'python', 'programacao', 'desenvolvimento', 'jogo', 'computador',
        'algoritmo', 'variavel', 'funcao', 'classe', 'objeto',
        'heranca', 'polimorfismo', 'interface', 'excecao', 'modulo',
        'pacote', 'biblioteca', 'sintaxe', 'compilador', 'interpretador',
        'debug', 'teste', 'unidade', 'recursao', 'loop',
        'condicional', 'array', 'lista', 'dicionario', 'tupla',
        'string', 'caractere', 'entrada', 'saida', 'arquivo',
        'sistema', 'rede', 'servidor', 'cliente', 'protocolo',
        'seguranca', 'criptografia', 'hash', 'banco', 'dados',
        'inteligencia', 'artificial', 'machine', 'learning', 'deep',
        'neural', 'rede', 'visualizacao', 'grafico', 'interface',
        'usuario', 'experiencia', 'design', 'desempenho', 'otimizacao'
    ]
    return random.choice(lista_palavras)



def mostra(palavra, letraadv):
    return' '.join(letra if letra in letraadv else '-' for letra in palavra)


def jogof():
    palavra = escolhe()
    letraadv = set()
    tentativas = 6


    print('Bem vindo ao jogo da forca')


    while tentativas > 0:
        print("\nPalavra:", mostra(palavra, letraadv))
        print(f"Tentativas restantes:{tentativas}")
        letra = input("Adivinhe uma letra: ").lower()


        if  letra in letraadv: 
            print("Vc ja tentou essa letra")
            continue
       
        letraadv.add(letra)


        if letra not in palavra:
            tentativas -= 1
            print(f"A letra {letra} não esta na palavra")


        if all(letra in letraadv for letra in palavra):
            print(f"Parabens vc advinhou, a palavra era: {palavra}")
            break
   
        elif tentativas <= 0:
            print(f"Voce perdeu, a palavra era {palavra}")


if __name__ == '__main__':
    jogof()