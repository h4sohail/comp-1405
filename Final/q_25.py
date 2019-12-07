from random import randint

dic = {}

for i in range(1000):
    random_key = randint(0,100)
    if random_key not in dic.keys():
        dic[random_key] = 1
    else:
        dic[random_key] += 1 

print(dic)