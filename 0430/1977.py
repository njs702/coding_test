import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

result = []

for i in range(M,N+1):
    # 약수의 개수가 홀수면 완전제곱수 아닐까
    temp_cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            temp_cnt += 1
    if temp_cnt % 2 != 0:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))

## 다른 방법 - i가 1부터 증가해가며 i^2 값이 M과 N 사이라면 리스트에 넣음