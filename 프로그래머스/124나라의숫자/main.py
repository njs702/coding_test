import sys

def solution(n):
    _list = []
    answer = ''
    
    while n:
        # n이 3의 배수일 때
        if n % 3 == 0:
            answer += "4"
            #_list.append("4")
            n = n // 3 - 1
        # n이 3의 배수가 아닐 때
        if n % 3 != 0:
            answer += str(n%3)
            #_list.append(str(n%3))
            n = n // 3
        
    # _list.reverse()
    # answer = "".join(_list)
    
    answer = answer[::-1]
    
    return answer