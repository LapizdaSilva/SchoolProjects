import pygame

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Casinha com PyGame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CINZA = (150, 150, 150)

fonte = pygame.font.SysFont('Arial', 36)

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    texto = fonte.render("SOL", True, BRANCO)
    
    tela.fill(PRETO)

    pygame.draw.rect(tela, VERMELHO, (300, 300, 200, 200))
    pygame.draw.polygon(tela, AMARELO, [(400, 200), (275, 300), (525, 300)]) 
    pygame.draw.rect(tela, BRANCO, (370, 400, 60, 100))  

    pygame.draw.ellipse(tela, AZUL, (320, 330, 40, 40))  

    pygame.draw.circle(tela, AMARELO, (100, 100), 50)
    tela.blit(texto, (70, 80))

    pygame.display.flip()

pygame.quit()
