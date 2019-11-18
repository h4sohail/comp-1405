def upper(string):
    lst = []
    new_lst = []
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            lst.append(char)
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(ord(lst[i]))

    return new_lst
print(upper('ABC'))