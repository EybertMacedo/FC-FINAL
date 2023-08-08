import pymunk
import pymunk.pygame_util
import pygame
import sys

pygame.init()


screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Máquina de Atwood con Pymunk")


white = (255, 255, 255)
black = (120, 60, 60)


space = pymunk.Space()
space.gravity = (0, -90)  


mass_1 = 100
mass_2 = 5
radius = 15
distance = 100
pulley_radius = 30


pulley_body = pymunk.Body(body_type=pymunk.Body.STATIC)
pulley_body.position = (screen_width // 2, screen_height // 2 + pulley_radius)
pulley_shape = pymunk.Circle(pulley_body, pulley_radius)
pulley_shape.friction = 0.8
space.add(pulley_body, pulley_shape)

body_1 = pymunk.Body(mass=mass_1, moment=5)
body_1.position = (screen_width // 2 - distance, screen_height // 2 + pulley_radius + distance)
circle_shape_1 = pymunk.Circle(body_1, radius)
circle_shape_1.friction = 0.8
space.add(body_1, circle_shape_1)

body_2 = pymunk.Body(mass=mass_2, moment=5)
body_2.position = (screen_width // 2 + distance, screen_height // 2 + pulley_radius + distance)
circle_shape_2 = pymunk.Circle(body_2, radius)
circle_shape_2.friction = 0.8
space.add(body_2, circle_shape_2)


joint = pymunk.SlideJoint(body_1, body_2, (0, 0), (0, 0), min=0, max=2*distance)
space.add(joint)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    space.step(1 / 60.0)

    
    screen.fill(white)

    
    for shape in space.shapes:
        if isinstance(shape, pymunk.Circle):
            pos_x, pos_y = shape.body.position
            pygame.draw.circle(screen, black, (int(pos_x), int(screen_height - pos_y)), radius)

    
    pygame.draw.circle(screen, black, (int(pulley_body.position.x), int(screen_height - pulley_body.position.y)), pulley_radius)

    
    pygame.draw.line(screen, black, (int(body_1.position.x), int(screen_height - body_1.position.y)),
                     (int(pulley_body.position.x), int(screen_height - pulley_body.position.y)), 2)
    pygame.draw.line(screen, black, (int(body_2.position.x), int(screen_height - body_2.position.y)),
                     (int(pulley_body.position.x), int(screen_height - pulley_body.position.y)), 2)

    
    pygame.display.flip()

    
    clock.tick(60)
