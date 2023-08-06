import pygame
pygame.init()

ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Ejemplo de Movimiento Rectilíneo")

color_bola = (187, 143, 206)

x_bola, y_bola = 50, alto // 2
velocidad_bola = 1

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    x_bola += velocidad_bola

    if x_bola >= ancho:
        x_bola = 0

    pantalla.fill((255, 255, 255))

    pygame.draw.circle(pantalla, color_bola, (x_bola, y_bola), 20)
    
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
