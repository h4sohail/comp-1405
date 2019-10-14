# Name: Hamza Sohail
# Student Number: 101168085

print('*****************************')
print('Welcome to the Magic Trail')
print('*****************************')

print('') # spacer

print('Pick your class')

# display the classes
print('\t [1] Ninja') 
print('\t [2] Wizard') 
print('\t [3] Sorceress') 

print('') # spacer

player_class_selection = int((input('Make your selection from the above classes: '))) # get the users choice and assign it to the 'player_class_selection' variable

if player_class_selection == 1: # if 'player_class_selection' variable is 1 then set the class to the first element in the classes list
    player_class = 'Ninja'
elif player_class_selection == 2: # if 'player_class_selection' variable is 2 then set the class to the second element in the classes list
    player_class = 'Wizard'
elif player_class_selection == 3: # if 'player_class_selection' variable is 3 then set the class to the third element in the classes list
    player_class = 'Sorceress'
else: # else return an error
    print('ERROR: Incorrect selection')

print('\t [-] You selected: {}'.format(player_class)) # display the selected class

print('') # spacer

player_name = input('Please enter your name: ') # get the player name and store it in the 'player_name' variable

print('\t [-] You entered: {}'.format(player_name)) # display the player name 

print('') # spacer

goblin_1_name = input("Please enter your first goblin's name: ") # get the first goblin's name and store it in the 'goblin_1_name' variable 
goblin_2_name = input("Please enter your second goblin's name: ") # get the second goblin's name and store it in the 'goblin_2_name' variable 
goblin_3_name = input("Please enter your third goblin's name: ") # get the third goblin's name and store it in the 'goblin_3_name' variable 

print('') # spacer

print('This is your adventure party')
print('\t [-] Your name: {}'.format(player_name)) # display the player name
print('\t [-] Your class: {}'.format(player_class)) # display the player class
print('\t [-] Your goblin\'s names are: {}, {} and {}'.format(goblin_1_name, goblin_2_name, goblin_3_name)) # display the globlin's names

print('') # spacer

print('Before leaving for your adventure make sure to grab some supplies') # show all the items in the market place

print('') # spacer

print('Welcome to the Adventurer\'s Black Market') # show all the items in the market place

print('\t-Potions-')
print('\t [-] Health Potion         | Effect: +10 HP              | Cost: 10 Gold Coin')
print('\t [-] Useless Potion        | Effect: None                | Cost: 100 Gold Coins')

print('\t-Elixirs-')
print('\t [-] Stamina Elixir        | Effect: +10 Stamina         | Cost: 20 Gold Coins')
print('\t [-] Mana Elixir           | Effect: +10 Mana            | Cost: 30 Gold Coins')
print('\t [-] Dark Energy Elixir    | Effect: +25 Mana            | Cost: 50 Gold Coins')

print('') # spacer

total_spent = 0 # counter for the total price

item_1 = int(input('How many Health Potions would you like to purchase: ')) # get the amount of items and store it in the 'item_1' variable
total_spent = item_1 * 10 # get the running total
print('\t [-] Gold coins spent so far: {:.2f}'.format(total_spent)) # display the running total

item_2 = int(input('How many Useless Potion would you like to purchase: ')) # get the amount of items and store it in the 'item_2' variable
total_spent += item_2 * 100 # get the running total
print('\t [-] Gold coins spent so far: {:.2f}'.format(total_spent)) # display the running total

item_3 = int(input('How many Stamina Elixirs would you like to purchase: ')) # get the amount of items and store it in the 'item_3' variable
total_spent += item_3 * 20 # get the running total
print('\t [-] Gold coins spent so far: {:.2f}'.format(total_spent)) # display the running total

item_4 = int(input('How many Mana Elixirs would you like to purchase: ')) # get the amount of items and store it in the 'item_4' variable
total_spent += item_4 * 30 # get the running total
print('\t [-] Gold coins spent so far: {:.2f}'.format(total_spent)) # display the running total

item_5 = int(input('How many Dark Energy Elixirs would you like to purchase: ')) # get the amount of items and store it in the 'item_5' variable
total_spent += item_5 * 50 # get the running total
print('\t [-] Gold coins spent so far: {:.2f}'.format(total_spent)) # display the total spent

print('') # spacer

print('-------------------------')
print('Adventurer\'s Black Market') # show all the items in the market place
print('-------------------------')
print('\t [-] 1. Health Potions         {:.2f}'.format(item_1 * 10)) # total spent on item 1
print('\t [-] 2. Useless Potions        {:.2f}'.format(item_2 * 100)) # total spent on item 2
print('\t [-] 3. Stamina Elixirs        {:.2f}'.format(item_3 * 20)) # total spent on item 3
print('\t [-] 4. Mana Elixirs           {:.2f}'.format(item_4 * 30)) # total spent on item 4
print('\t [-] 5. Dark Energy Elixirs    {:.2f}'.format(item_5 * 50)) # total spent on item 5
print('-------------------------')
print('\t Total: {:.2f} Gold Coins'.format(total_spent)) # display the total spent