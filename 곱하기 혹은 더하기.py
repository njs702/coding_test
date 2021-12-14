import re

S = input()

#input 값을 정수로 변환하기(굳이 안해도 됨)
str_numbers = re.findall("\d",S)
int_numbers = list(map(int,str_numbers))
print(int_numbers)
result = int_numbers[0]

#result와 num 둘 중 하나라도 1 이하라면 더하기 연산 수행하기
for i in range(1,len(int_numbers)):
  num = int_numbers[i]
  if result <= 1 or num <= 1:
    result = result + num
  else:
    result = result * num


print(result)