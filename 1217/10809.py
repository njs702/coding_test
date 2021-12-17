n = input()
alphabet = list(range(97,123)) # a-z가 97부터 122(아스키코드값)

for x in alphabet:
    print(n.find(chr(x)),end=" ") # find함수 => 문자열에서 사용가능, 해당하는 문자가 어느 위치에 있는지 리턴
