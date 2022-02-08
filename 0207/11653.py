import sys

N = int(sys.stdin.readline())
number_list = []
temp_num = 2

if N == 1:
    pass
else:
    while N != 1:        
        if N % temp_num == 0:
            number_list.append(temp_num)
            N //= temp_num
        else:
            temp_num += 1

number_list.sort()
for number in number_list:
    print(number)