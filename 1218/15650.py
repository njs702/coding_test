# N과 M (2)

n,m = map(int,input().split())
numbers = []

def dfs(start):
    if len(numbers) == m: # depth가 m인 부분까지 탐색을 했다면
        print(' '.join(map(str,numbers))) # 출력 후 탈출
        return
    
    for i in range(start,n+1): 
        if i in numbers: # 가지치기, 이미 탐색을 한 노드라면 건너뛴다
            continue
        
        numbers.append(i) # dfs의 기본, 넣고
        dfs(i + 1) # 깊이까지 탐색을 마치고 // i보다 큰 수만 하면 된다
        numbers.pop() # 탐색한 노드 꺼내기


dfs(1)

    