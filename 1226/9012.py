import sys

n = int(sys.stdin.readline())
for i in range(n):
    vps = sys.stdin.readline()
    vps = list(vps)
    sum = 0
    for j in vps:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0: # )가 더 많은 경우
            print("NO")
            break
    if sum > 0: # (가 더 많은 경우
        print("NO")
    elif sum == 0:
        print("YES")