from rendering_math import convert_point
import sys
import pygame
import math

def drawPoint(point):
    p = convert_point(point, cam, cam_angle, w, h)
    if p:
        pygame.draw.circle(screen, red, p, 2)

def drawLine(points):
    p1 = convert_point(points[0], cam, cam_angle, w, h)
    p2 = convert_point(points[1], cam, cam_angle, w, h)

    pygame.draw.line(screen, red, p1, p2)


pygame.init()

w, h = 1000, 500
black = (0, 0, 0)
red = (255, 0, 0)

cam = [0, 0, 0] 

cam_angle = (0, 0, 0)

points = [(-0.5, 0, 1), (0.5, 0, 1), (-0.5, 0, 2), (0.5, 0, 2), (-0.5, 1, 1), (0.5, 1, 1), (-0.5, 1, 2), (0.5, 1, 2), ]

lines = [[points[0], points[1]], 
[points[0], points[2]], 
[points[2], points[3]], 
[points[3], points[1]], 

[points[4], points[5]], 
[points[4], points[6]], 
[points[5], points[7]], 
[points[6], points[7]], 

[points[0], points[4]], 
[points[1], points[5]], 
[points[2], points[6]], 
[points[3], points[7]], 
]

screen = pygame.display.set_mode((w, h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                cam[1] = cam[1] - 0.1

            if event.key == pygame.K_LSHIFT:
                cam[1] = cam[1] + 0.1

            if event.key == pygame.K_d:
                cam[0] = cam[0] + 0.1

            if event.key == pygame.K_a:
                cam[0] = cam[0] - 0.1

            if event.key == pygame.K_w:
                cam[2] = cam[2] + 0.1

            if event.key == pygame.K_s:
                cam[2] = cam[2] - 0.1


    screen.fill(black)

    for point in points:
        drawPoint(point)        

    for line in lines:
        drawLine(line)

    pygame.display.flip()