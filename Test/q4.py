# Create a 2d grid, 'y' by 'z' list with random even values from a query

import random

def has_even(query): # (Edgecase) Incase there are no evens in the query
    query = query.strip()
    lst = query.split(',')
    for num in lst:
        if int(num) % 2 == 0:
            return True
    return False

def evens(query):
    evens = []
    nums = query.strip().split(',')
    for num in nums:
        if int(num) % 2 == 0:
            evens.append(num)
    return evens

def random_even(lst):
    return lst[random.randint(0, len(lst)-1)]
 
        
def grid(query, y, z):
    grid = []
    if has_even(query): # (Edgecase) Incase there are no evens in the query
        for i in range(y):
            row = []
            for j in range(z):
                row.append(random_even(evens(query)))
            grid.append(row)

        for row in grid:
            print(row)
    else:
        return grid

query = '1,3,4,5,6,7,8,9 '
y = 3
z = 4

# Generate a 3x4 grid of random even integers from the query 

grid(query, y, z)