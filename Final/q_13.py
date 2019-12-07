lst_2d = [[1,2,3], [4,5,6]]

def print_2d(lst_2d):
    for lst in lst_2d:
        for item in lst:
            print(item, end=' ')
        print()

print_2d(lst_2d)

def print_grid(a_list ):
    for i in range(len(a_list)):
        for j in range (len(a_list[i])):
            print(a_list[i][j] , end =" ")
        print()

print_grid(lst_2d)
