# y x z list
# '1,2,3,4,5,6, '
# 2 x 2

# Output:
# 2 6
# 4 6

# Strip the input string
# values are random even numbers from input
# Create a 2d 'y' by 'z' list with values

import random

def has_even(string):
    string = string.strip()
    lst = string.split(',')
    for num in lst:
        if int(num) % 2 == 0:
            return True
    return False

def random_evens(string):
    string = string.strip()
    lst = string.split(',')
    while(True):
        random_index = random.randint(0, len(lst)-1)
        if int(lst[random_index]) % 2 == 0:
            return lst[random_index]

def make_lst(string, y, z):
    lst_2d = []
    if has_even(string):
        for i in range(y):
            row = []
            for j in range(z):
                random_even = random_evens(string)
                row.append(random_even)
            lst_2d.append(row)

        for i in range(len(lst_2d)):
            print(lst_2d[i])
    else:
        return lst_2d

string = '1,3,4,5,6,7,8,9,10 '
y = 4
z = 3

make_lst(string, y, z)

