import sys

n = int(sys.stdin.readline())
count = 1
stack = []
opers = []
flag = 0

# 1부터 n까지의 숫자를 스택에 넣어가며 연산
for i in range(n):
    number = int(sys.stdin.readline())
    # count가 입력받은 숫자를 만날 때 까지 stack에 push
    while count <= number:
        stack.append(count)
        opers.append("+")
        count += 1
        
    # stack에 있는 마지막 숫자가 입력받은 숫자와 같다면 꺼낸다.
    if stack[-1] == number:
        stack.pop()
        opers.append("-")
    
    # 만약 마지막 숫자와 다르다면, 오름차순으로 들어온 것이 아니기 때문에 만들 수 없는 수열이 된다.
    else:
        print("NO")
        flag = 1 # 만들 수 없는 상태라는 것을 알려주는 flag
        break

# 만약 수열을 만들 수 있다면, 저장되어 있는 operation 출력
if flag == 0:
    for oper in opers:
        print(oper)
    