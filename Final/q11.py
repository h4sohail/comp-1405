n = int( input (" Which n-th value of the Fibonacci Sequence do you wish to know ? "))

def fib(n):
    val_1 = 0
    val_2 = 1
    if n == 1:
        return 1
    else:
        for i in range (n - 1):
            val_1, val_2 = val_2, val_1 + val_2
        return val_1
print(fib(n))
