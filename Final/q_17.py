lst_2d = [[1,'2',3], [4,5,6]]

def double(lst_2d):
    for i in range(len(lst_2d)):
        for j in range(len(lst_2d[i])):
            lst_2d[i][j] = lst_2d[i][j] * 2
    return lst_2d

print(double(lst_2d))

