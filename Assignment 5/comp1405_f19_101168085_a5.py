# Name: Hamza Sohail
# Student Number: 101168085


def upper(string):
    """
    Converts all the characters in a list to an upper case character by subtracting 32 from it's ASCI value

    Args:
        str: The original string input  
    Returns:
        string: Returns the same string but capitalized
    """
    new_string = '' # Empty string to append to
    for char in string: # Itterate over each character in user's string
        if char.isalpha() and not char.isupper(): # If the character is an alphabet and not already uppercase
            char = (chr(ord(char) - 32)) # Subtract 32 from it's ASCI value to get the uppercase alphabet
        if char.isalnum() or char == ' ': # Preserve spaces, and ignore special characters such as punctuation etc.
            new_string += char # Append capitalized characters and spaces to the new string
    return new_string # return the capitalized string


def phrases(string):
    """
    Changes some predefined phrases in a string

    Args:
        str: The original string input 
    Returns:
        string: Returns the same string but certain phrases are changed by acronyms
    """

    string = upper(string) # pass the string to the upper function to capitalize it
    string_list = string.split() # split the string by spaces into a list

    for i in range(len(string_list)): # Itterate over words in the list
        if len(string_list) >= 3: # Edgecase (if userinput is too short)
            if string_list[i] == 'BY' and string_list[i+1] == 'THE' and string_list[i+2] == 'WAY': # Check if the string "BY THE WAY" appears in the list
                string_list[i] = 'BTW' # Change the first occurence in list to 'BTW'
                string_list[i+1] = '' # Change the second occurence in list to an empty character
                string_list[i+2] = '' # Change the third occurence in list to an empty character

            if string_list[i] == 'YOU' and string_list[i+1] == 'ARE' and string_list[i+2] == 'WELCOME': # Check if the string "YOU ARE WELCOME" appears in the list
                string_list[i] = 'YW' # Change the first occurence in list to 'YW'
                string_list[i+1] = '' # Change the second occurence in list to an empty character
                string_list[i+2] = '' # Change the third occurence in list to an empty character

            if string_list[i] == 'ON' and string_list[i+1] == 'MY' and string_list[i+2] == 'WAY': # Check if the string "ON MY WAY" appears in the list
                string_list[i] = 'OMW' # Change the first occurence in list to 'OMW'
                string_list[i+1] = '' # Change the second occurence in list to an empty character
                string_list[i+2] = '' # Change the third occurence in list to an empty character

        elif len(string_list) >= 2: # Edgecase (if userinput is too short)
            if string_list[i] == 'NO' and string_list[i+1] == 'PROBLEM': # Check if the string "NO PROBLEM" appears in the list
                string_list[i] = 'NP' # Change the first occurence in list to 'NP'
                string_list[i+1] = '' # Change the second occurence in list to an empty character
    
    new_string_list = [] # New empty array to store words without the empty characters
    for word in string_list: # Itterate over words in the list
        if word != '': # if the word is not an empty character
            new_string_list.append(word) # append the word to the new list
    
    new_string = ' '.join(new_string_list) # Join the list to a string
    return new_string # Return the string


def words(string):
    """
    Changes some predefined words in a string 

    Args:
        str: The original string input 
    Returns:
        string: Returns the same string but certain words are changed by acronyms
    """
    string = upper(string) # pass the string to the upper function to capitalize it
    string_list = string.split() # split the string by spaces into a list
    
    for i in range(len(string_list)): # Itterate over words in the list
        if len(string_list) >= 1: # Edgecase (if userinput is too short)
            if string_list[i] == 'EASY': # Check if the string "EASY" appears in the list
                string_list[i] = 'EZ' # Replace it with EZ

            elif string_list[i] == 'NICE': # Check if the string "NICE" appears in the list
                string_list[i] = 'NYC' # Replace it with "NYC"

            elif string_list[i] == 'LATER': # Check if the string "LATER" appears in the list
                string_list[i] = 'L8R' # Check if the string "L8R" appears in the list

            elif string_list[i] == 'THANKS': # Check if the string "THANKS" appears in the list
                string_list[i] = 'TY' # Replace it with "TY"
    
    new_string = ' '.join(string_list) # Join the list to a string
    return new_string # Return the new string


def letters(string, user_input):
    """
    Changes some letters in a string 

    Args:
        str: The original string input 
        str: The characters that need to be replaced
    Returns:
        string: Returns the same string but certain letters are changed by homoglyps
    """

    string = upper(string) # pass the string to the upper function to capitalize it
    options = [] # The array where the options given by the user will be stored
    new_string = '' # Empty string to append to

    for char in user_input: # Itterate over words in the options passed by the user 
        options.append(char) # Append them to the options list

    for char in string: # Itterate over each character in the original string
        if char == 'A' and 'A' in options: # If the character is "A" and given by the user
            char = '4' # Repalce it with "4"
        if char == 'E' and 'E' in options: # If the character is "E" and given by the user
            char = '3' # Repalce it with "3"
        if char == 'S' and 'S' in options: # If the character is "A" and given by the user
            char = '5' # Repalce it with "5"
        if char == 'B' and 'B' in options: # If the character is "B" and given by the user
            char = '13' # Repalce it with "13"
        if char == 'O' and 'O' in options: # If the character is "O" and given by the user
            char = '0' # Repalce it with "0"
        if char == 'I' and 'I' in options: # If the character is "I" and given by the user
            char = '1' # Repalce it with "1"
        if char == 'V' and 'V' in options: # If the character is "V" and given by the user
            char = '\/' # Repalce it with "\/"
        if char == 'W' and 'W' in options: # If the character is "W" and given by the user
            char = '\/\/' # Repalce it with "\/\/"
        new_string += char # Append all the characters to the empty string

    return new_string # Return the new string


def main():
    """
    Converts the phrases, words and characters in a string based on user input
    """
    
    while True: # Loop to restart the program
        options = ['A', 'E', 'S', 'B', 'O', 'I', 'V', 'W'] # List of characters that can be replaced 
        choices = ['YES', 'NO'] # List of choices allowed for the user
        
        user_original = input('Type the string to be translated: \n') # Get the original string from the user
        user_text = upper(user_original) # Save the original string in a different variable
        user_text_phrases = upper(user_original) # Default value incase the user does not want to change phrases
        user_text_words = upper(user_original) # Default value incase the user does not want to change words

        print(upper(user_text)) # Print the string capitalized

        user_phrase = upper(input('Do you want to replace phrases?: ')) # Ask if the user wants to change phrases

        while user_phrase not in choices: # Check if the user gave a valid reply
            user_phrase = upper(input('Please enter yes or no. Do you want to replace phrases?: '))

        if user_phrase == 'YES': # If the user said yes
            user_text_phrases = phrases(user_text) # Change phrases in the string by passing the string to the phrases function
            user_text = user_text_phrases # Set the string to the new string returned by the phrases function

        user_words = upper(input('Do you want to replace words?: ')) # Ask if the user wants to change the words
        while user_words not in choices: # Check if the user gave a valid reply
            user_words = upper(input('Please enter yes or no. Do you want to replace words?: '))

        if user_words == 'YES': # If the user said yes
            user_text_words = words(user_text) # Change the words in the string by passing the string to the phrases function
            user_text = user_text_words # Set the string to the new string returned by the words function

        user_letters = upper(input('Do you want to replace letters?: ')) # Ask if the user wants to replace letters
        while user_letters not in choices: # Check if the user gave a valid reply
            user_letters = upper(input('Please enter yes or no. Do you want to replace letters?: '))

        if user_letters == 'YES': # If the user said yes
            user_letters = upper(input('What letters do you want to replace?: ')) # Ask the user what characters they would like to replace
            for letter in user_letters: # Check if the characters they selected are changeable
                if letter not in options: # If they are not changeable tell them 
                    print('This program can not replace \'{}\' '.format(letter))
            user_text = letters(user_text, user_letters) # Pass the original string and the characters to be replaced to the letters function

        print('\nString for translation: {}'.format(upper(user_original))) # Show the original string uppercased
        print('After replacing phrases: {}'.format(user_text_phrases)) # Show the string after replacing phrases
        print('After replacing words: {}'.format(user_text_words)) # Show the string after replacing words
        print('After replacing letters: {}'.format(user_text)) # Show the string after replacing letters
        print('The fully translated string is: \'{}\'\n'.format(user_text)) # Show the final translated string

        new_string = upper(input('Do you want to translate another string?: ')) # Ask the user if they would like to restart the program
        while new_string not in choices: # Check if the user gave a valid reply
            new_string = upper(input('Please enter yes or no. Do you want to translate another string?: '))
        
        if new_string == 'NO': # If the user said no
            print('Sorry to see you go. Goodbye.') # Print a sad message
            break # Break the loop to end the program


# Entry point of the program
if __name__ == '__main__':
	main() # call the main function if this file is the entry point