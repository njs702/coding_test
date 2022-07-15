T = int(input())

money = [50000,10000,5000,1000,500,100,50,10]
result_count = [0,0,0,0,0,0,0,0]

def func(n,i):
    result_count = [0,0,0,0,0,0,0,0]
    while n != 0:
        if n >= 50000:
            n -= 50000
            result_count[0] += 1
            continue
        if n >= 10000:
            n -= 10000
            result_count[1] += 1
            continue
        if n >= 5000:
            n -= 5000
            result_count[2] += 1
            continue
        if n >= 1000:
            n -= 1000
            result_count[3] += 1
            continue
        if n >= 500:
            n -= 500
            result_count[4] += 1
            continue
        if n >= 100:
            n -= 100
            result_count[5] += 1
            continue
        if n >= 50:
            n -= 50
            result_count[6] += 1
            continue
        if n >= 10:
            n -= 10
            result_count[7] += 1
            continue
    print(f'#{i+1}')
    print(*result_count)
    
for i in range(T):
    N = int(input())
    N = N - (N%10)
    func(N,i)