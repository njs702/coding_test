N = input()
len_n = len(N)
N = int(N)
count = 0

# N = 4 , 0 1 2 
for i in range(len_n-1):
    # 1부터 9까지 : 9개 x 자리수(1)
    # 10부터 99까지 : 90개 x 자리수(2)
    # 100부터 999까지 : 900개 x 자리수(3)
    # 9 * 10^(i) * len
    count += 9 * (10**i) * (i+1)

for i in range(10**(len_n-1),N+1):
    count = count + len_n 

print(count)