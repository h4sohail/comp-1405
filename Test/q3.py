string = "This iS the First question on your Second quiz."
def capital_words(string):
    lst = string.split()
    new_lst = []
    for word in lst:
        for char in word:
            if char.isupper():
                new_lst.append(word)
    return new_lst

print(capital_words(string))