lst = [1,45,10,35,100,13,147,500,80]

def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

print(selection_sort(lst))    


                
        
                
