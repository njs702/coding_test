import sys

n = int(input())
numbers = list(map(int,sys.stdin.readline().split()))

numbers.sort() # 투포인터 사용하기 위한 정렬
# [-99, -2, -1, 4, 98]
start, end = 0, n-1
val1, val2 = 0, n-1
min = abs(numbers[0] + numbers[-1])
result = []
result.append([numbers[start],numbers[end]])

if numbers[0] >= 0:
    print(numbers[0],numbers[1])

elif numbers[-1] < 0:
    print(numbers[-2],numbers[-1])

else:
    while start < end:
        temp_sum = 0
        temp_sum = abs(numbers[start] + numbers[end])
        # start 증가시켰을 때 합과 end 증가시켰을 때 합을 비교해서 
        # 합이 작은 쪽으로 start 또는 end 이동시키기?
        if temp_sum < min:
            min = temp_sum
            result.append([numbers[start],numbers[end]])
            
        if abs(numbers[start + 1] + numbers[end]) <= abs(numbers[start] + numbers[end-1]):
            start += 1
        else:
            end -= 1
    print(result[-1][0],result[-1][1])
