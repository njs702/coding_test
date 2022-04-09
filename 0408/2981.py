import sys
import math

N = int(sys.stdin.readline())
numbers = []
sub_numbers = []
div_numbers = []

for _ in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)
numbers.sort()

# N[0] = K[0] * M + R
# N[1] = K[1] * M + R
# N[2] = K[2] * M + R
# N[3] = K[3] * M + R

# N[1] - N[0] = M * (K[1] - K[0])
# N[2] - N[1] = M * (K[2] - K[1])
# N[3] - N[2] = M * (K[3] - K[2])

# M은 N[1] - N[0], N[2] - N[1] , ... , N[n] - N[n-1]의
# 최대공약수의 약수이다.

# 6 34 38인 경우
# 34 - 6 = 28 -> 1,2,4,7,14,28
# 38 - 34 = 4 -> 1,2,4
# 공통된 것 : 2,4 즉 최대공약수 4의 약수 임을 알 수 있다.

for i in range(1,N):
    sub_numbers.append(numbers[i]-numbers[i-1])

_gcd = sub_numbers[0]
for sub_number in sub_numbers:
    _gcd = math.gcd(_gcd,sub_number)

# 약수를 찾을 떄, 해당 숫자의 제곱근 이하 까지만 구하는 것을 통해 시간 절약
for i in range(1,int((_gcd**0.5)) + 1):
    if _gcd % i == 0:
        div_numbers.append(i)
        div_numbers.append(_gcd//i)

result = set(div_numbers)
result = list(result)
result.sort()
result.pop(0)
print(*result)