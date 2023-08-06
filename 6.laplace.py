import pymunk
import pymunk.pygame_util
import pygame
import sys
import random
import math


width, height = 800, 600


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, 0


thermal_diffusivity = 0.5  


static_body = space.static_body
border_points = [(0, 0), (0, height), (width, height), (width, 0)]
border_segments = [pymunk.Segment(static_body, border_points[i], border_points[(i + 1) % 4], 1) for i in range(4)]
for segment in border_segments:
    segment.elasticity = 1.0
    segment.friction = 1.0
    space.add(segment)

particles = []
for x in range(0, width, 40):
    for y in range(0, height, 40):
        particle_body = pymunk.Body(1, 1)
        particle_body.position = x, y
        
        distance_to_center = ((x - width / 2) ** 2 + (y - height / 2) ** 2) ** 0.5
        particle_body.temp = max(100 - distance_to_center * 0.5, 0)
        particle_shape = pymunk.Circle(particle_body, 5)
        space.add(particle_body, particle_shape)
        particles.append(particle_body)


def propagate_heat(particles, thermal_diffusivity):
    new_temperatures = {}
    for body in particles:
        x, y = body.position
        temp_diff = 0
        for neighbor_body in particles:
            if neighbor_body != body:
                neighbor_x, neighbor_y = neighbor_body.position
                distance_sq = (neighbor_x - x) ** 2 + (neighbor_y - y) ** 2
                temp_diff += (neighbor_body.temp - body.temp) / distance_sq
        new_temp = body.temp + thermal_diffusivity * temp_diff
        new_temperatures[body] = new_temp

    
    for body in particles:
        body.temp = new_temperatures[body]


def get_color_by_temperature(temperature):
    
    normalized_temp = (temperature - 0) / (100 - 0)
    
    r = int(normalized_temp * 255)
    g = 0
    b = int((1 - normalized_temp) * 255)
    return r, g, b


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    propagate_heat(particles, thermal_diffusivity)

    
    screen.fill((255, 255, 255))
    for segment in border_segments:
        pygame.draw.line(screen, (0, 0, 0), segment.a, segment.b, 2)
    for body in particles:
        color = get_color_by_temperature(body.temp)
        pygame.draw.circle(screen, color, body.position, 5)
        font = pygame.font.Font(None, 18)
        temp_text = font.render(str(int(body.temp)), True, (0, 0, 0))
        screen.blit(temp_text, (body.position[0] + 10, body.position[1] - 10))

    
    space.step(1 / 60.0)
    pygame.display.flip()
    clock.tick(60)
