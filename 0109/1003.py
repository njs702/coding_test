import sys

count_zero = 0
count_one = 0

def fibo(n):
    global count_zero
    global count_one
    
    if n == 0:
        count_zero += 1
        return 0
    elif n == 1:
        count_one += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(sys.stdin.readline())
for i in range(n):
    number = int(sys.stdin.readline())
    fibo(number)
    print(count_zero, count_one)
    count_zero = 0
    count_one = 0

