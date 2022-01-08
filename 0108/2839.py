import sys

sugar = int(sys.stdin.readline())
bag = 0
 
while sugar >= 0: # 입력값이 0 이상일 때 까지 반복
    if sugar % 5 == 0: # 5의 배수라면, 5로 나누는 것이 개수 optimal
        bag += sugar // 5 # 가방 개수 더하기
        print(bag)
        break
    sugar -= 3 # 만약 5의 배수가 아니면, 3을 감소해 가면서 5의 배수가 될 때 까지 빼기
    bag += 1 # 가방의 개수 1개 증가
    
else: # 설탕이 5와 3으로 정확히 만들 수 없음
    print(-1)
    
        
