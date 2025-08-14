import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Casinha com Partes Móveis")
clock = pygame.time.Clock()

# Cores
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19) 
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)

# Posições iniciais
corpo_x, corpo_y = 200, 310  
telhado_x, telhado_y = 300, 280  
janela_x, janela_y = 100, 500 
porta_x, porta_y = 200, 130  
chamine_x, chamine_y = 300, 200

# Função de rotação
def rotate_surface(surface, angle, center):
    rotated_surface = pygame.transform.rotate(surface, angle)
    rotated_rect = rotated_surface.get_rect(center=center)
    return rotated_surface, rotated_rect

chamine_angle = 0  # Inicializa o ângulo da chaminé

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimento do corpo
    if keys[pygame.K_a]: corpo_x -= 2.5
    if keys[pygame.K_d]: corpo_x += 2.5
    if keys[pygame.K_w]: corpo_y -= 2.5
    if keys[pygame.K_s]: corpo_y += 2.5

    # Movimento do telhado
    if keys[pygame.K_LEFT]: telhado_x -= 2.5
    if keys[pygame.K_RIGHT]: telhado_x += 2.5
    if keys[pygame.K_UP]: telhado_y -= 2.5
    if keys[pygame.K_DOWN]: telhado_y += 2.5

    # Movimento da janela
    if keys[pygame.K_j]: janela_x -= 2.5
    if keys[pygame.K_l]: janela_x += 2.5
    if keys[pygame.K_i]: janela_y -= 2.5
    if keys[pygame.K_k]: janela_y += 2.5

    # Movimento da porta 
    if keys[pygame.K_f]: porta_x -= 2.5
    if keys[pygame.K_h]: porta_x += 2.5
    if keys[pygame.K_t]: porta_y -= 2.5
    if keys[pygame.K_g]: porta_y += 2.5
    
    # Rotação da chaminé
    if keys[pygame.K_c]:
        chamine_angle += 2

    # Desenho
    screen.fill(BLACK)

    # Corpo da casa
    corpo_rect = pygame.Rect(corpo_x - 50, corpo_y - 50, 100, 100)
    pygame.draw.rect(screen, BLUE, corpo_rect)

    # Criação da surface da chaminé
    chamine_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
    chamine_surface.fill((0, 0, 0, 0))  # transparente
    pygame.draw.rect(chamine_surface, PURPLE, (10, 0, 20, 40))  # desenha chaminé centralizada

    # Gira e desenha a chaminé
    rotated_chamine, chamine_rect = rotate_surface(chamine_surface, chamine_angle, (chamine_x, chamine_y))
    screen.blit(rotated_chamine, chamine_rect)

    # Telhado
    telhado_points = [
        (telhado_x - 70, telhado_y + 50),
        (telhado_x + 70, telhado_y + 50),
        (telhado_x, telhado_y - 50)
    ]
    pygame.draw.polygon(screen, RED, telhado_points)

    # Janela
    janela_rect = pygame.Rect(janela_x - 15, janela_y - 15, 30, 30)
    pygame.draw.rect(screen, YELLOW, janela_rect)

    # Porta
    porta_rect = pygame.Rect(porta_x - 10, porta_y - 20, 20, 40)
    pygame.draw.rect(screen, BROWN, porta_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
