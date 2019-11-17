# Name: Hamza Sohail
# Student Number: 101168085


def upper(string):
    new_string = ''
    for char in string:
        if char.isalpha() and not char.isupper():
            char = (chr(ord(char) - 32))
        if char.isalnum() or char == ' ':
            new_string += char
    return new_string


def phrases(string):
    string = upper(string)
    string_list = string.split()

    for i in range(len(string_list)):
        if len(string_list) >= 3:
            if string_list[i] == 'BY' and string_list[i+1] == 'THE' and string_list[i+2] == 'WAY':
                string_list[i] = 'BTW'
                string_list[i+1] = ''
                string_list[i+2] = ''

            if string_list[i] == 'YOU' and string_list[i+1] == 'ARE' and string_list[i+2] == 'WELCOME':
                string_list[i] = 'YW'
                string_list[i+1] = ''
                string_list[i+2] = ''

            if string_list[i] == 'ON' and string_list[i+1] == 'MY' and string_list[i+2] == 'WAY':
                string_list[i] = 'OMW'
                string_list[i+1] = ''
                string_list[i+2] = ''

        elif len(string_list) >= 2:
            if string_list[i] == 'NO' and string_list[i+1] == 'PROBLEM':
                string_list[i] = 'NP'
                string_list[i+1] = ''
    
    new_string_list = []
    for word in string_list:
        if word != '':
            new_string_list.append(word)
    
    new_string = ' '.join(new_string_list)
    return new_string


def words(string):
    string = upper(string)
    string_list = string.split()
    
    for i in range(len(string_list)):
        if len(string_list) >= 1:
            if string_list[i] == 'EASY':
                string_list[i] = 'EZ'

            elif string_list[i] == 'NICE':
                string_list[i] = 'NYC'

            elif string_list[i] == 'LATER':
                string_list[i] = 'L8R'

            elif string_list[i] == 'THANKS':
                string_list[i] = 'TY'
    
    new_string_list = []
    for word in string_list:
        if word != '':
            new_string_list.append(word)
    
    new_string = ' '.join(new_string_list)
    return new_string


def letters(string, user_input):
    string = upper(string)
    options = []
    new_string = ''
    for char in user_input:
        options.append(char)

    for char in string:
        if char == 'A' and 'A' in options:
            char = '4'
        if char == 'E' and 'E' in options:
            char = '3'
        if char == 'S' and 'S' in options:
            char = '5'
        if char == 'B' and 'B' in options:
            char = '13'
        if char == 'O' and 'O' in options:
            char = '0'
        if char == 'I' and 'I' in options:
            char = '1'
        if char == 'V' and 'V' in options:
            char = '\/'
        if char == 'W' and 'W' in options:
            char = '\/\/'
        new_string += char

    return new_string


# this is the definition of your main function
def main():
    while True:
        options = ['A', 'E', 'S', 'B', 'O', 'I', 'V', 'W']
        choices = ["YES", "NO"]
        
        user_original = input("Type the string to be translated: \n")
        user_text = user_original
        
        print(upper(user_text))

        user_phrase = upper(input("Do you want to replace phrases? \n"))

        while user_phrase not in choices:
            user_phrase = upper(input("Please enter yes or no. Do you want to replace phrases? \n"))

        if user_phrase == 'YES':
            user_text_phrases = phrases(user_text)
            user_text = user_text_phrases

        user_words = upper(input("Do you want to replace words? \n"))
        while user_words not in choices:
            user_words = upper(input("Please enter yes or no. Do you want to replace words? \n"))

        if user_words == 'YES':
            user_text_words = words(user_text)
            user_text = user_text_words

        user_letters = upper(input("Do you want to replace letters? \n"))
        while user_letters not in choices:
            user_letters = upper(input("Please enter yes or no. Do you want to replace letters? \n"))

        if user_letters == 'YES':
            user_letters = upper(input("What letters do you want to replace? \n"))
            for letter in user_letters:
                if letter not in options:
                    print("This program can not replace '{}' ".format(letter))
            user_text = letters(user_text, user_letters)

        print("\nString for translation: {}".format(upper(user_original)))
        print("After replacing phrases: {}".format(user_text_phrases))
        print("After replacing words: {}".format(user_text_words))
        print("After replacing letters: {}".format(user_text))
        print("The translated string is: '{}' \n".format(user_text))

        new_string = upper(input("Do you want to translate another string? \n"))
        
        if new_string == 'NO':
            print("Goodbye.")
            break


# these should be the last two lines of your submission
if __name__ == '__main__':
	main()