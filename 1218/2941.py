alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="] # 크로아티아 알파벳

words = input()

def num_of_alphabet(words):
    for i in alphabet: # 모든 크로아티아 알파벳에 대해
        words = words.replace(i,"*") # replace 함수는 문자열에 같은 문자열 부분을 모두 대체하는 것
    return len(words)

print(num_of_alphabet(words))