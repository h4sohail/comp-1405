def ceil(num):
    if num//1 == num:
        return int(num)
    else:
        return int((num//1) + 1)

print(ceil(1.9))