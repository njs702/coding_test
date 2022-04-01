import sys
from collections import deque

T = int(input())
for _ in range(T):
    
    cnt = 0
    queue = deque()
    target_queue = deque()
    
    N,M = map(int,sys.stdin.readline().split())
    target_list = [0]*N
    # root = [1,2,3,4]
    root = list(map(int,input().split(" ")))
    # 뽑아야 할 obj = root[2] = 3
    print_obj = root[M]
    
    # 뽑아야 할 obj를 똑같은 크기의 queue에 target 문자열로 선언해준다
    target_list[M] = 'target'
    
    
    ## target 큐와 입력 큐 선언 부분 ## target queue = [0,0,'target',0]
    for i in range(N):
        target_queue.append(target_list[i]) 
    
    for i in range(N):
        queue.append(root[i])
    ## target 큐와 입력 큐 선언 부분 ## 입력 queue = [1,2,3,4]
    
    while True:   
        flag = False # 뽑아야 할지 말아야 할지 판단하는 변수
        
        # N = 1이면 그냥 가장 앞에있는놈 뽑고 마무리
        if N == 1:
            cnt += 1
            break
        
        # N이 2 이상일 때 알고리즘
        else:
            # 큐에 자기 자신보다 큰 수가 하나라도 있는지 판단하는 반복문
            for i in range(1,N):
                if queue[0] < queue[i]: # 만약 하나라도 자기보다 큰 수가 있다 -> 뽑지 말고 뒤로 보내야 한다
                    flag = False # 뽑지 말아야 함
                    queue.rotate(-1) # 뒤로보내기
                    target_queue.rotate(-1) # 뒤로보내기
                    break
            # 반복문을 다 돌았는데도 큰 수가 없다? -> 뽑아야 한다, flag = True
            else:
                flag = True

            # 만약 뽑아야 하는 상황이고, 젤 앞에 있는 수가 뽑아야 할 target이 아닌 경우
            # --> 그냥 뽑아버리면 된다
            if flag == True and target_queue[0] != 'target':
                queue.popleft() # 뽑기
                target_queue.popleft() # 뽑기
                N -= 1 # 큐 크기 감소
                cnt += 1 # 뽑았으니 count 증가
                flag = False # 다시 뽑아야 할지 말아야 할지 판단하기 위해 false로 변경
            
            # 만약 뽑아야 하는 상황이고, 젤 앞에 있는 수가 숫자가 같고 target이라면, 처음에 설정한 숫자를 뽑는 경우
            if flag == True and queue[0] == print_obj and target_queue[0] == 'target':
                queue.popleft() # 뽑는다
                N -= 1 # 큐의 인수 개수 감소
                cnt += 1 # 뽑았으니 count 증가
                break # 원하는 수를 뽑았으므로 while문 탈출
            
    print(cnt)  
        

        
    
    