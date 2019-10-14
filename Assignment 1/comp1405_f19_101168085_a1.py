# Name: Hamza Sohail
# Student Number: 101168085

import pygame # import pygame library

pygame.display.init() # initialize pygame display

#variables for width and height of our main window
screen_width = 500 
screen_height = 500 

#variables used to hold color tuples as (r, g, b) values
white = (255, 255, 255) # white, color code: #FFFFFF 
black = (0, 0, 0) # black, color code: #000000 
red = (255, 0 ,0) # red, color code: #FF0000 
green = (0, 255, 0) # green, color code: #008000 
blue = (0, 0, 255) # blue, color code: #0000FF 
yellow = (255, 255, 0) # yellow, color code: #FFFF00  
brown = (165, 42, 42) # brown, color code: #A52A2A 
wood_brown = (150, 111, 51) # wood_brown, color code: #966F33

screen = pygame.display.set_mode([screen_width, screen_height]) # initialize the surface and set size from our width and height variables
screen.fill(white) # set background color to white

#sun (top right)
center = (450,50) 
radius = 40 
pygame.draw.circle(screen, yellow, center, radius) # draw a yellow circle centered at (450,50) with a radius of 40

#outer house (rectangle)
x_cord = 200 
y_cord = 200 
rect_width = 250 
rect_height = 150 
thickness = 4 
pygame.draw.rect(screen, blue,(x_cord, y_cord, rect_width, rect_height), thickness) # draw a blue rectangle with the top left point at (200,200) with a width of 250 and height of 150, and thickness of 4

#roof (line)
spatial_points = [(200,200), (262.5,150), (325, 200)] 
thickness = 4 
pygame.draw.lines(screen, red, False, spatial_points, thickness) # draw a red line between the points (200,200), (262.5,150), (325, 200) with a thickness of 4

#chimney (rectangle)
x_cord = 425 
y_cord = 150 
rect_width = 15 
rect_height = 50 
thickness = 4 
pygame.draw.rect(screen, brown,(x_cord, y_cord, rect_width, rect_height), thickness) # draw a brown rectangle with the top left point at (425,150) with a width of 15 and height of 50, and thickness of 4

#left door frame (line)
spatial_points = [(300,300), (300,350)] 
thickness = 3 
pygame.draw.lines(screen, black, False, spatial_points, thickness) # draw a black line between the points (300,300), (300,350) with a thickness of 3

#right door frame (line)
spatial_points = [(340,300), (340,350)] 
thickness = 3 
pygame.draw.lines(screen, black, False, spatial_points, thickness) # draw a black line between the points (340,300), (340,350) with a thickness of 3

#door handle (line)
center = (310,320) 
radius = 2
pygame.draw.circle(screen, black, center, radius) # draw a black circle centered at (310,320) with a radius of 2

#glass panel above door (arc)
pi = 3.14159 # approximation of mathmatical constant 'pi'
thickness = 3 
pygame.draw.arc(screen, black, (300,280,41,60), 0, pi, thickness) # draw a black arc centered at (300,200) starting from angle 0 to pi with a thickness of 3

#panel frame above door (line)
spatial_points = [(300,300), (340,300)] 
thickness = 1
pygame.draw.lines(screen, black, False, spatial_points, thickness) # draw a black line between the points (300,300), (340,300) with a thickness of 1

#window frame (line)
spatial_points = [(250,200), (250,250), (200, 250)] 
thickness = 4
pygame.draw.lines(screen, black, False, spatial_points, thickness) # draw a black line between the points (250,200), (250,250), (200, 250) with a thickness of 4   

#window horizontal panel (line)
spatial_points = [(200,225), (250,225)] 
thickness = 1 
pygame.draw.lines(screen, black, False, spatial_points, thickness) # draw a black line between the points (200,225), (250,225) with a thickness of 1

#window vertical panel (line)
spatial_points = [(225,200), (225,250)] 
thickness = 1 
pygame.draw.lines(screen, black, False, spatial_points, thickness) # draw a black line between the points (225,200), (225,250) with a thickness of 1

#tree leaves (circle)
center = (70,250) 
radius = 68 
pygame.draw.circle(screen, green, center, radius) # draw a green circle centered at (70,250)  with a radius of 68

#tree trunk (polygon)
spatial_points = [(70,400), (65,300), (64, 295)] 
poly_width = 20 
pygame.draw.polygon(screen, wood_brown, spatial_points, poly_width) # draw a wood brown polygon connected by the points (70,400), (65,300), (64, 295) with a width of 20

#tree branch 1 (polygon)
spatial_points = [(65,300), (40,250), (35, 240)] 
poly_width = 4 
pygame.draw.polygon(screen, wood_brown, spatial_points, poly_width) # draw a wood brown polygon connected by the points (65,300), (40,250), (35, 240) with a width of 4

#tree branch 2 (polygon)
spatial_points = [(65,325), (75,240), (78, 240)] 
poly_width = 5 
pygame.draw.polygon(screen, wood_brown, spatial_points, poly_width) # draw a wood brown polygon connected by the points (65,325), (75,240), (78, 240) with a width of 5

pygame.display.update() # refresh the screen to display our changes

pygame.image.save(screen, 'house_101168085.bmp') # save image from the main display as house_studentId.bmp

pygame.time.wait(3000) # delay further program execution by 3 seconds

pygame.quit() # exit pygame