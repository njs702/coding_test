n,k = map(int,input().split())
coins = []
count = 0
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
for coin in coins:
    if coin <= k: # 금액 같아야 한다
        temp = k // coin
        count += temp
        k = k % coin # 내가 했던 코드 : k -= coin * temp // 실행오류(테스트케이스 오류)
    

print(count)