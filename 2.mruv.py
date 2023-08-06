import pygame


pygame.init()


ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Ejemplo de MRUV")


color_bola = (255, 0, 0)


x_bola, y_bola = 50, alto // 2
velocidad_bola = 0
aceleracion_bola = 0.2


reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    
    velocidad_bola += aceleracion_bola
    x_bola += velocidad_bola

    
    if x_bola >= ancho:
        x_bola = 0

    
    pantalla.fill((255, 255, 255))

    
    pygame.draw.circle(pantalla, color_bola, (int(x_bola), y_bola), 20)

    
    pygame.display.flip()

    
    reloj.tick(60)


pygame.quit()
