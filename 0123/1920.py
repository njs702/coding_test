import sys

n_numbers = []
m_numbers = []
n = int(sys.stdin.readline())
n_numbers = list(map(int,sys.stdin.readline().split()))
n_numbers.sort() # 이분 탐색을 위한 정렬
m = int(sys.stdin.readline())
m_numbers = list(map(int,sys.stdin.readline().split()))

def binary_search(n_numbers,find):
    start = 0
    end = len(n_numbers) - 1
    while start <= end: 
        mid = (start + end) // 2
        if find == n_numbers[mid]:
            return 1
        elif find > n_numbers[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0
    
for m in m_numbers:
    print(binary_search(n_numbers,m))