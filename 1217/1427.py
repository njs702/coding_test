# 소트인사이드

n = input()
list = list(map(int,n))
list.sort(reverse=True)
for i in list:
    print(i,end="")