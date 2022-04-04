import sys
from collections import deque

# R : 뒤집기
# D : 첫 번째 수 버리기, 비어있을 때 D 하면 error

T = int(sys.stdin.readline())
for _ in range(T):
    flag = False
    rev_num = 0
    order = sys.stdin.readline()
    N = int(sys.stdin.readline())
    numbers = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    # print(numbers)
    if N == 0:
        numbers = deque()
    
    for i in range(len(order)):
        if order[i] == 'R':
            # reverse함수의 시간 복잡도 때문에 시간 초과가 남
            # reverse는 두번하면 그대로이기 떄문에, R의 개수가 홀수일 경우에만 reverse 해주면 된다.
            rev_num += 1 
        if order[i] == 'D':
            if len(numbers) == 0:
                flag = True
                print("error")
                break
            if rev_num % 2 == 0:
                # rev_num이 짝수면 배열 그대로기 때문에 왼쪽거를 뽑고
                numbers.popleft()
            else:
                # rev_num이 홀수면 배열이 뒤집어졌기 때문에 오른쪽을 뽑는다
                numbers.pop()
                
    if flag == False and rev_num % 2 == 0:
        print('['+','.join(numbers)+']')
    if flag == False and rev_num % 2 == 1:
        numbers.reverse()
        print('['+','.join(numbers)+']')
        
    