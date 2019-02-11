from display import *
from draw import *
import math

screen = new_screen()

def rotate(px, py, rx, ry, angle):
    theta = math.radians(angle)
    newX = int((px - rx) * math.cos(theta) - (py - ry) * math.sin(theta))
    newY = int((py - ry) * math.cos(theta) + (px - rx) * math.sin(theta))
    return [newX + rx, newY + ry]

def makeTri(centerX, centerY, d, angle, color):
    startX = rotate(centerX, centerY + d, centerX, centerY, angle)[0]
    startY = rotate(centerX, centerY + d, centerX, centerY, angle)[1]
    for i in range(3):
        rotatedX = rotate(startX, startY, centerX, centerY, -120)[0]
        rotatedY = rotate(startX, startY, centerX, centerY, -120)[1]
        draw_line(startX, startY, rotatedX, rotatedY, screen, color)
        startX = rotatedX
        startY = rotatedY

draw_line(250,0,250,500,screen,[229, 185, 0])
draw_line(0,250,500,250,screen,[229, 185, 0])
draw_line(0,0,500,500,screen,[229, 185, 0])
draw_line(0,500,500,0,screen,[229, 185, 0])

distance = 250
angle = 0
color = [229, 185, 0]
while distance >= 0:
    makeTri(250, 250, distance, angle, color)
    distance -= 2
    angle -= 10
    color = [229, 70 + int(115 * (distance/250)), 0]





# prevX = 250
# prevY = 250
# for y in range(500):
#     for x in range(500):
#         if abs(10000 - (pow(x - 250, 2) + pow(y - 250, 2))) <= 25:
#             # print ("Current point: " + '(' + str(x) + ',' + str(y) + ')')
#             # print ("Last point: " + '(' + str(prevX) + ',' + str(prevY) + ')')
#             draw_line(250, 250, x, y, screen, color)
#             draw_line(prevX, prevY, x, y, screen, color)
#             prevX = x
#             prevY = y

display(screen)
save_extension(screen, 'img.png')
