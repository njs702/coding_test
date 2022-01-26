import sys

# 5층 1 7 28 84 ...
# 4층 1 6 21 56 126 252
# 3층 1 5 15 35 70 126
# 2층 1 4 10 20 35 56 84
# 1층 1 3 6 10 15 21 28
# 0층 1 2 3 4 5 6 7

array = []

def func(k,n,array_0):
    global array
    array.append(array_0)
    # k층에 있는 방들의 사람을 구하는 과정
    for i in range(1,k+1):
        # temp_list에는 해당 층의 사람 수 정보가 담김
        temp_list = []
        # 특정 층에서 각 방들에 존재하는 사람들의 수를 저장하는 배열
        for j in range(1,n+1):
            count = 0 
            temp_sum = 0
            # j번째 호에 존재하는 사람 수를 구하기 위한 과정
            # 이전 층의 j번째까지 존재하는 사람들의 수를 더해야 함
            while count != j:
                temp_sum += array[i-1][count]
                count += 1
            # 해당 층의 정보들을 저장 , temp_sum = j번째 호에 존재하는 사람 수
            temp_list.append(temp_sum)
        # 아파트 전체 정보에 저장
        array.append(temp_list)
    print(array[k][n-1])
    array = []
            
T = int(sys.stdin.readline())


for _ in range(T):
    k = int(sys.stdin.readline()) # k층
    n = int(sys.stdin.readline()) # n호
    array_0 = [i for i in range(1,n+1)]
    func(k,n,array_0)
