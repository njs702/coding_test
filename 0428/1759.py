import sys

# 서로 다른 L개의 알파벳으로 구성된 문자열 찾기
L,C = map(int,sys.stdin.readline().split())
alphabets = list(sys.stdin.readline().split())
_result = []
alphabets.sort()
visited = [False for _ in range(C)]

compare_con = ['a','e','i','o','u']

# 자음
con = []

# 모음
vow = []

# 최소 한 개의 모음(a,e,i,o,u)
# 최소 두 개의 자음

def dfs(start):
    global compare_con
    # 길이가 맞고, 최소 한개의 모음과 두 개의 자음이 있다면 출력
    if len(_result) == L and len(con) >= 2 and len(vow) >= 1:
        print("".join(_result))
        return
    
    for i in range(start,C):
        if visited[i]: continue
        
        _result.append(alphabets[i])
        if alphabets[i] in compare_con:
            vow.append(alphabets[i])
        else:
            con.append(alphabets[i])
        visited[i] = True
        dfs(i+1)
        temp = _result.pop()
        if temp in con:
            con.remove(temp)
        if temp in vow:
            vow.remove(temp)
        visited[i] = False

dfs(0)
        
