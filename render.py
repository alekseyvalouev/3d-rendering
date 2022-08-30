from rendering_math import *
import sys
import pygame
import keyboard
import numpy as np
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

cam = (0, 0, 0) 

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

    speed = 0.005
    
    up = (0, speed, 0)
    down = (0, -speed, 0)
    fwd = (0, 0, speed)
    back = (0, 0, -speed)
    left = (-speed, 0, 0)
    right = (speed, 0, 0)

    if keyboard.is_pressed(" "):
        cam = np.add(cam, rotate_vector(down, cam_angle))

    if keyboard.is_pressed("cmd"):
        cam = np.add(cam, rotate_vector(up, cam_angle))

    if keyboard.is_pressed("d"):
        cam = np.add(cam, rotate_vector(right, cam_angle))

    if keyboard.is_pressed("a"):
        cam = np.add(cam, rotate_vector(left, cam_angle))

    if keyboard.is_pressed("w"):
        cam = np.add(cam, rotate_vector(fwd, cam_angle))

    if keyboard.is_pressed("s"):
        cam = np.add(cam, rotate_vector(back, cam_angle))

    #if keyboard.is_pressed("down"):
    #   cam_angle = np.add(cam_angle,  (-1*math.pi/3600, 0, 0))

    #if keyboard.is_pressed("up"):
    #    cam_angle = np.add(cam_angle,  (1*math.pi/3600, 0, 0))

    if keyboard.is_pressed("left"):
        cam_angle = np.add(cam_angle,  (0, -1*math.pi/3600, 0))

    if keyboard.is_pressed("right"):
        cam_angle = np.add(cam_angle,  (0, math.pi/3600, 0))

    screen.fill(black)

    for point in points:
        drawPoint(point)        

    for line in lines:
        drawLine(line)

    pygame.display.flip()