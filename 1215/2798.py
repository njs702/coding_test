# 블랙잭

n,m = map(int,input().split())
cards = list(map(int,input().split()))

cards.sort()
result = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if cards[i] + cards[j] + cards[k] <= m and cards[i] + cards[j] + cards[k] >= result:
                result = cards[i] + cards[j] + cards[k]
                
print(result)
