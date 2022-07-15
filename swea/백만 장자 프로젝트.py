T = int(input())

def func(list,i):
    # 마지막 날부터 계산하기
    # 마지막 날 판매 금액 기준으로 시작
    sum = 0
    cur = list[-1]
    for i in range(len(list)-1,-1,-1):
        # 현재 판매가격보다 작다면 현재 판매가격으로 파는것이 이득
        if list[i] < cur:
            sum += cur
            sum -= list[i]
        # 현재 판매가격보다 크다면, 그날엔 그날의 금액으로 파는것이 이득
        else:
            cur = list[i]
    print(f'#{i+1}',end = " ")
    print(sum)
        

for i in range(T):
    my_list = []
    N = int(input())
    my_list = list(map(int,input().split()))
    func(my_list,i)
    