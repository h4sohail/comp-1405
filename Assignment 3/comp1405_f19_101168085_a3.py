# Name: Hamza Sohail
# Student Number: 101168085

#--------------------------------#
# [Sub-Genre: Crime Films]
#--------------------------------#

# [yes, yes]
# "The Godfather" – italian mob, crime family 

# [yes, no]
# "Goodfellas" –  italian mob, no crime family

# [no, yes, yes]
# "The Highwaymen" – no italian mob, police, couple

# [no, yes, no]
# "Training Day" – no italian mob, police, no couple

# [no, no, yes, yes]
# "Legend" – no italian mob, no police, crime duo, twins

# [no, no, yes, no]
# "Pulp Fiction" – no italian mob, no police, crime duo, no twins

# [no, no, no, yes]
# "Catch Me If You Can" –  no italian mob, no police, no crime duo, impersonator

# [no, no, no, no, yes]
# "Oceans Twelve" – no italian mob, no police, no crime duo, no impersonator, heists

# [no, no, no, no, no, yes]
# "Memento" –  no italian mob, no police, no crime duo, no impersonator, no heists, memory loss

# [no, no, no, no, no, no]
# "Scarface" – no italian mob, no police, no crime duo, no impersonator, no heists, no memory loss, no heists

#--------------------------------#
# [Sub-Genre: Super-Heroes]
#--------------------------------#
# [yes, yes]
# "Ironman" - billionaire, flies 

# [yes, no]
# "Batman" - billionaire, doesn't fly 

# [no, yes, yes]
# "Hulk" - not a billionaire, changes size, changes colour

# [no, no, no]
# "Antman" - not billionaire, change sizes, doesn't change colour

# [no, no, yes, yes]
# "Endgame" - not billionaire, doesn't change sizes, has a hammer, has a gauntlet

# [no, no, yes, no]
# "Thor" - not billionaire, doesn't change sizes, has a hammer, doesn't have a gauntlet

# [no, no, no, yes]
# "Doctor Strange" - not billionaire, doesn't change sizes, doesn't have a hammer, uses magic

# [no, no, no, no, yes]
# "Superman" - not billionaire, doesn't change sizes, doesn't have a hammer, doesn't use magic, laser eyes

# [no, no, no, no, no, yes]
# "Captain America: The First Avenger" - not billionaire, doesn't change sizes, doesn't have a hammer, doesn't use magic, doesn't have laser eyes, has a shield 
# 
# [no, no, no, no, no, no]
# "Deadpool" - # "Captain America: The First Avenger" - not billionaire, doesn't change sizes, doesn't have a hammer, doesn't use magic, doesn't have laser eyes, no shield 


instructions_choice = input('Do you want instructions? yes/no: ').lower() # ask the user for their selection and make it lowercase
if instructions_choice == 'yes': # if user enters yes show instructions
    print('Choose a Sub-Genre and then answer the questions with a "yes" \n'
          'or a "no" so the expert system can guess the movie.\n')

exit_condition = False # boolean value used to check the while loop to exit if needed     
while(exit_condition == False): # while loop to keep asking the user for input if the exit_condition is False
    print('Sub-Genres:')
    print('1. Crime Films\n2. Super-Heroes')
    sub_genre = input('Please select the Sub-Genre: ') # get the sub-genre selection of the user
    
    if sub_genre == '1': # if they enter '1' set sub genre to Crime Films
        print('You selected: Crime Films\n')

        choice = input('Is the movie based on the Italian mob?: ').lower() 
        if choice == 'yes': 
            choice = input('Does the movie revolve around a crime family?: ').lower() 
            if choice == 'yes':
                print('Your movie is The Godfather')
                exit_choice = input('Do you want to quit? yes/no: ').lower() # get the answer for the question
                if exit_choice == 'yes': # ask the user if they want to exit
                    break # break the loop if yes
                else:
                    continue # keep looping if no
            
            else:
                print('Your movie is Goodfellas') 
                exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                if exit_choice == 'yes':
                    break # break the loop if yes 
                else:
                    continue # keep looping if no
        else:      
            choice = input('Is the movie based on the police?: ').lower() 
            if choice == 'yes':
                choice = input('Does the movie have a criminal couple?: ').lower() 
                if choice == 'yes':
                    print('Your movie is The Highwaymen')
                    exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                    if exit_choice == 'yes': 
                        break # break the loop if yes 
                    else:
                        continue # keep looping if no
                else:
                    print('Your movie is Training Day')
                    exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                    if exit_choice == 'yes':
                        break # break the loop if yes
                    else:
                        continue # keep looping if no

            else:     
                choice = input('Does the movie have a crime duo?: ').lower() 
                if choice == 'yes':
                    choice = input('Are the two main characters twins?: ').lower() 
                    if choice == 'yes':
                        print('Your movie is Legend')
                        exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                        if exit_choice == 'yes':
                            break # break the loop if yes
                        else:
                            continue # keep looping if no
                    else:
                        print('Your movie is Pulp Fiction')
                        exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                        if exit_choice == 'yes':
                            break # break the loop if yes
                        else:
                            continue # keep looping if no
                        
                else:
                    choice = input('Is the main character an impersonator?: ').lower() 
                    if choice == 'yes':    
                        print('Your movie is Catch Me If You Can')
                        exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                        if exit_choice == 'yes':
                            break # break the loop if yes
                        else:
                            continue # keep looping if no
                    else:
                        choice = input('Does the movie revolve around heists?: ').lower()  
                        if choice == 'yes':
                            print('Your movie is Oceans Twelve')
                            exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                            if exit_choice == 'yes':
                                break # break the loop if yes
                            else:
                                continue # keep looping if no
                        else:
                            choice = input('Does the main character have memory loss?: ').lower() 
                            if choice == 'yes':
                                    print('Your movie is Memento')
                                    exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                                    if exit_choice == 'yes':
                                        break # break the loop if yes
                                    else:
                                        continue # keep looping if no
                            else:                           
                                print('Your movie is Scarface')
                                exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                                if exit_choice == 'yes':
                                    break # break the loop if yes 
                                else:
                                    continue # keep looping if no

    elif sub_genre == '2': # if they enter '2' set sub genre to Super-Heroes
        print('You selected: Super-Heroes\n')

        choice = input('Is the main character a billionaire?: ').lower() 
        if choice == 'yes':
            choice = input('Does the main character fly?: ').lower() 
            if choice == 'yes':
                print('Your movie is Ironman')
                exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                if exit_choice == 'yes':
                    break # break the loop if yes
                else:
                    continue # keep looping if no
            
            else:
                print('Your movie is Batman')
                exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                if exit_choice == 'yes':
                    break # break the loop if yes
                else:
                    continue # keep looping if no
        else:      
            choice = input('Does the main character change size when they fight?: ').lower() 
            if choice == 'yes':
                choice = input('Does the main character change color when they fight?: ').lower() 
                if choice == 'yes':
                    print('Your movie is Hulk')
                    exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                    if exit_choice == 'yes':
                        break # break the loop if yes
                    else:
                        continue # keep looping if no
                else:
                    print('Your movie is Antman')
                    exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                    if exit_choice == 'yes':
                        break # break the loop if yes
                    else:
                        continue # keep looping if no 

            else:     
                choice = input('Does one of the characters have a hammer?: ').lower() 
                if choice == 'yes':
                    choice = input('Does one of the characters have a gauntlet?: ').lower()
                    if choice == 'yes':
                        print('Your movie is Endgame')
                        exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                        if exit_choice == 'yes':
                            break # break the loop if yes
                        else:
                            continue # keep looping if no 
                    else:
                        print('Your movie is Thor')
                        exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                        if exit_choice == 'yes':
                            break # break the loop if yes
                        else:
                            continue # keep looping if no
                        
                else:
                    choice = input('Do the main character use magic?: ').lower()
                    if choice == 'yes':    
                        print('Your movie is Doctor Strange')
                        exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                        if exit_choice == 'yes':
                            break # break the loop if yes
                        else:
                            continue # keep looping if no
                    else:
                        choice = input('Does the main character have laser eyes?: ').lower()  
                        if choice == 'yes':
                            print('Your movie is Superman')
                            exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                            if exit_choice == 'yes':
                                break # break the loop if yes
                            else:
                                continue # keep looping if no
                        else:
                            choice = input('Does the main character have a shield?: ').lower()   
                            if choice == 'yes':
                                    print('Your movie is Captain America')
                                    exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                                    if exit_choice == 'yes':
                                        break # break the loop if yes
                                    else:
                                        continue # keep looping if no 
                            else:                           
                                print('Your movie is Deadpool')
                                exit_choice = input('Do you want to quit? yes/no: ').lower() # ask the user if they want to exit
                                if exit_choice == 'yes':
                                    break # break the loop if yes
                                else:
                                    continue # keep looping if no 
    else:
        exit_condition = True # exit the loop if the input was not '1' or '2'

