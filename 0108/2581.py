import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
numbers = []
prime_numbers = []
sum = 0
count = 0

for i in range(n,m+1):
    numbers.append(i)

for number in numbers:
    for i in range(1,number+1):
        if(number % i ==0):
            count += 1
    if count == 2:
        prime_numbers.append(number)
    count = 0

for prime_number in prime_numbers:
    sum += prime_number

if prime_numbers:
    print(sum)
    print(min(prime_numbers))
else:
    print(-1)
    
 