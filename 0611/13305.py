n = int(input())
cost = 0

distance = list(map(int,input().split()))
prices = list(map(int,input().split()))

# ex) 도시의 기름값이 [10, 8, 4, 9, 2] 라고 주어졌다

minimum = prices[0] # 현재 기름값의 최소값 min = 10

for i in range(n):
    if prices[i] > minimum: # 만약 방문하는 도시의 기름값이 최소값보다 크다면 
        prices[i] = minimum # 해당 도시의 기름값을 최소값으로 변경(이전에 있던 도시의 최소값으로 기름을 사면 됨)
    else:
        minimum = prices[i] # 만약 방문 도시가 최소값이라면, 최소값으로 변경 min =8, min = 4 ....

# 결과적으로 도시의 기름값 리스트는 [10,8,4,4,2]로 변경

for i in range(n-1):
    cost += prices[i] * distance[i] # 

print(cost)
