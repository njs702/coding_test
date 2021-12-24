while True:
    n,k = map(int,input().split())
    if n == 0 and k == 0:
        break
    else:
        if k % n == 0:
            print('factor')
        elif n % k == 0:
            print('multiple')
        else:
            print('neither')