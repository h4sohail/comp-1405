#Write some code below that asks the user for a sentence, removes all punctuation
#marks and commas, then replaces all white spaces with underscores. Afterwards, make a call to
#print to output the final result to the user. You are permitted to use the following functions: strip.
#You are NOT permitted to use the replace function.


def str_clean(string):
    new_str = ''
    string = string.strip()
    for char in string:
        if char not in ['.', '!', '?']:
            if char == ' ':
                char = '_'
            new_str += char
        
    return new_str

string = input('input: ')
print(str_clean(string)) 