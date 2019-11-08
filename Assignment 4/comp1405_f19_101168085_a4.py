# Name: Hamza Sohail
# Student Number: 101168085

import pygame # importing pygame 

pygame.display.init() # intitialize display module
pygame.font.init() # intitialize the font module

instructions_choice = input('Do you need instructions?: ').lower() # ask the user for their selection and make it lowercase
if instructions_choice == 'yes': # if user enters yes show instructions
    print('Type the filename of the background image you would like to use \n'
          'and then specify which ghost image you would like to overlay on top\n'
          'finally, you can either use your mouse or the terminal provide the \n'
          'coordinates of where you would like the ghost to appear\n')

background_filename = input('Type the file name of the background image you would like to use: ') # get the background file name
background_image = pygame.image.load(background_filename) # load the above image into pygame as an image
(screen_width, screen_height) = background_image.get_rect().size # get the dimensions of the background image and save it into a tuple

ghost_file = input('Type the file name of the ghost image you would like to use: ') # get the ghost image file
ghost_image = pygame.image.load(ghost_file) # load the above image into pygame as an image
(ghost_width, ghost_height) = ghost_image.get_rect().size # get the dimensions of the ghost image and save it into a tuple

screen = pygame.display.set_mode([screen_width, screen_height]) # intialize the pygame screen with the dimensions of the background image
screen.blit(background_image, (0, 0)) # set the background of the screen 
pygame.display.update() # refresh the screen to display the background

exit_condition = True # exit condition for the loop
while(exit_condition): # start the main loop for handling input and drawing

    choice = int(input('Type \'1\' to use the terminal or \'2\' to use your mouse to input the ghost cordinates: ')) # ask the user for the choice of input type
    if choice == 1: # if the users enters 1, take input from the console
        x_cordinate = int(input('Type the x cordinate of where you want to overlay the ghost image: ')) # get the x cordinate from the user
        y_cordinate = int(input('Type the y cordinate of where you want to overlay the ghost image: ')) # get the y cordinate from the user
        if x_cordinate < 0 or x_cordinate > screen_width: # check if the x cordinate is valid and not outside the bounds of the screen
            print('Invalid x cordinate')
            continue
        elif y_cordinate < 0 or y_cordinate > screen_height: # check if the y cordinate is valid and not outside the bounds of the screen
            print('Invalid y cordinate')
            continue
        break

    elif choice == 2: # if the user enters 2, take the input from the mouse
        # get mouse input here
        font_object = pygame.font.SysFont('Arial', 32) # load the Arial font from the system
        green = (0, 255, 0) # green color code
        black = (0, 0, 0) # black color code

        while(True): # start the loop for the 
            pygame.event.get() # without this method being called the screen becomes unresponsive, talked to the prof, it's a potential bug

            (mouse_x, mouse_y) = pygame.mouse.get_pos() # get the mouse position and save it in a tuple
            mouse_pos = font_object.render(f'X: {mouse_x} Y:{mouse_y}', True, green, black) # initialize a font render to draw the x,y cordinates of the mouse, with a green text color and black background color
            screen.blit(mouse_pos, (mouse_x, mouse_y)) # draw the mouse position (same place as the cursor) on the screen with the x,y position of the mouse
            pygame.display.update() # update the display to show the changes
            x_cordinate = mouse_x # set the cordinate for the ghost the same as the x cordinate of the mouse
            y_cordinate = mouse_y # set the cordinate for the ghost the same as the y cordinate of the mouse

            screen.blit(background_image, (0, 0)) # re-add the background image to refresh it
 
            left_click = pygame.mouse.get_pressed()[0] # get the left click value, from the list of mouse buttons returned by pygame.mouse.get_pressed
            if left_click: # check if the left click was pressed
                exit_condition = False # set the exit condition for the outer loop
                break # break inner loop
    else:
        print('Invalid choice') # invalid choice
        continue # reset the loop for them to enter their choice again

for i in range(ghost_width): # loop for each row of pixels in the ghost image
    for j in range(ghost_height): # loop for the each pixel in the row in the ghost image
        (red, green, blue, _) = ghost_image.get_at((i, j)) # get each pixels color and save it in a tuple
        if (red, green, blue) != (0, 255, 0): # check if the pixel is green
            green_x_cordinate = x_cordinate - int((ghost_width/2)) + i # offset the x cordinate to place the new pixel at the center of the point selected by the user  
            green_y_cordinate = y_cordinate - int((ghost_height/2)) + j # offset the y cordinate to place the new pixel at the center of the point selected by the user 
            
            if not(green_x_cordinate <= 0 or green_y_cordinate <= 0): # (edge case) dont try to average the rgb value when the pixel is off the screen
                if not(green_x_cordinate >= screen_width or green_y_cordinate >= screen_height): # same edge case as above, just split it into two statements for clarity
                    (red_b, green_b, blue_b, _) = background_image.get_at((green_x_cordinate, green_y_cordinate)) # get the rgb value of the pixel from the background image
                    average_rgb = ((red + red_b)/2, (green + green_b)/2, (blue + blue_b)/2) # average the rgb values of the two pixels
                    screen.set_at([green_x_cordinate, green_y_cordinate], average_rgb) # assign the new averaged rgb value to the offset cordinates           

pygame.display.update() # update the screen to draw the ghost

while True: # code copied from assignment specifications, used to exit the game properly
    for event in pygame.event.get(): # get all the events from pygame
        if event.type == pygame.QUIT: # check if there was a QUIT event
            pygame.quit() # quit pygame
            pygame.display.update() # update the display


