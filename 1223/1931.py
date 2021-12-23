from typing import MutableSet


n = int(input())
meetings = []
count = 0

for i in range(n):
    meetings.append(list(map(int,input().split())))
meetings = sorted(meetings,key=lambda x:x[0]) # 회의 시작 시간을 기준으로 오름차순 정렬
meetings = sorted(meetings,key=lambda x:x[1]) # 회의 시작 시간 기준 오름차순 정렬 되 있는 상태에서, 끝 시간 기준으로 오름차순 정렬

last = 0 # 회의의 마지막 시간 저장

for meeting in meetings:
    start = meeting[0] # 회의 시작시간
    end = meeting[1] # 회의 끝나는시간
    
    if start >= last: # 회의 시작시간이 이전 회의 끝나는 시간보다 크거나 같다면
        count += 1 # 수 증가
        last = end # 회의 끝나는 시간 = 현재 회의가 끝나는 시간

print(count)