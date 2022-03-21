import sys
# 분할 정복 문제

A,B,C = map(int,sys.stdin.readline().split())

# A^(m+n) = A^m * A^n
# (A X B) % C = (A%C)*(B%C)%C

# 2^10 = 2^5 * 2^5 (지수가 짝수)
# 2^11 = 2^5 * 2^5 * 2 (지수가 홀수)

def DaC(a,b):
    global C
    if b == 1:
        return a % C
    
    temp = DaC(a,b//2)
    
    # 짝수라면 temp * temp
    if b % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * a % C
    
print(DaC(A,B))