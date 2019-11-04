import pygame # importing a semi useless library (again)

pygame.display.init() # intitialize display

print('Dear TA/Professor, Assignments like this do not teach you the essence of programming, instead it just teaches how to painfully debug external libraries.')
print('This is an introduction to CS course, we should not have to worry about 6 hours of debugging/trial and error with PyGame.')
print('This library has many bugs, from simple issues with trying to close or move the window, to weird OS related issues with optimizations and it\'s graphics engine!')
print('Instead if we were taught to use just the standard library of Python and it\'s immense set of features, we would be far better programmers.')
print('We have not even covered simple structures like dictionaries, yet we are diving deep into PyGame\'s feature set for some odd reason.')
print('If I had known this section would be like this, I would have transfered to different section.')
print('I am not in GameDEV, don\'t force me to use PyGame.\n\n')

instructions_choice = input('Do you need instructions?: ').lower() # ask the user for their selection and make it lowercase
if instructions_choice == 'yes': # if user enters yes show instructions
    print('Type the filename of the background image you would like to use \n'
          'and then specify which ghost image you would like to overlay on top\n'
          'finally, provide the coordinates of where you would like the ghost to appear\n')

background_filename = input('Type the file name of the background image you would like to use: ') 
background_image = pygame.image.load(background_filename)
(screen_width, screen_height) = background_image.get_rect().size

ghost_file = input('Type the file name of the ghost image you would like to use: ')
ghost_image = pygame.image.load(ghost_file)
(ghost_width, ghost_height) = ghost_image.get_rect().size

while(True):
    x_cordinate = int(input('Type the x cordinate of where you want to overlay the ghost image: '))
    y_cordinate = int(input('Type the y cordinate of where you want to overlay the ghost image: '))
    if x_cordinate < 0 or x_cordinate > screen_width:
        print('Invalid x cordinate')
        continue
    elif y_cordinate < 0 or y_cordinate > screen_height:
        print('Invalid y cordinate')
        continue
    else:
        break

for i in range(ghost_width):
    for j in range(ghost_height):
        (red, green, blue, _) = ghost_image.get_at((i, j))
        if (red, green, blue) != (0, 255, 0):
            green_x_cordinate = x_cordinate - int((ghost_width/2)) + i   
            green_y_cordinate = y_cordinate - int((ghost_height/2)) + j
            
            if not(green_x_cordinate <= 0 or green_y_cordinate <= 0):
                if not(green_x_cordinate >= screen_width or green_y_cordinate >= screen_height):
                    (red_b, green_b, blue_b, _) = background_image.get_at((green_x_cordinate, green_y_cordinate))
                    average_rgb = ((red + red_b)/2, (green + green_b)/2, (blue + blue_b)/2)
                    background_image.set_at([green_x_cordinate, green_y_cordinate], average_rgb)
            

screen = pygame.display.set_mode([screen_width, screen_height])
screen.blit(background_image, (0, 0))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.display.update()


