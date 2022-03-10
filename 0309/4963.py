import sys
from collections import deque

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]

board = []

def bfs(x,y):
    land_queue = deque()
    land_queue.append((x,y))
    board[x][y] = 0
    
    while land_queue:
        a,b = land_queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                board[nx][ny] = 0
                land_queue.append((nx,ny))
                
                # board[nx][ny] = land_counter
                #land_counter = land_counter + 1
    

while True:
    board = []
    land_counter = 0
    w,h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    for _ in range(h):
        board.append(list(map(int,sys.stdin.readline().split())))
    
    for x in range(h):
        for y in range(w):
            if board[x][y] == 1:
                bfs(x,y)
                land_counter += 1

    # print()
    # for a in board:
    #     for j in a:
    #         print(j,end=" ")
    #     print()
    print(land_counter)
                
    
    
