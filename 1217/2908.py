array = list(input().split())

rnum1 = array[0][::-1]
rnum2 = array[1][::-1]

print(max(int(rnum1),int(rnum2)))