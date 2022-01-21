import sys

count = 2
sum = 1
n = int(sys.stdin.readline())

# 6개, 12개, 18개 ....

# 1 (1개)
# 2~7 (6개) count 2
# 8~19(12개) count 3
# 20~37(18개) count 4
# 38~61(24개) count 5
pivot = 1

if n == 1:
    print(1)
else:
    while True:
        if sum >= n:
           print(count-1)
           break
        sum += 6 * (count-1)
        count += 1 
       

