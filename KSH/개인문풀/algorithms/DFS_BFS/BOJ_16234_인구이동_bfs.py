from collections import deque
import sys

initial_set, *country = [list(map(int, line.split()))for line in sys.stdin.readlines()]
N, L, R = initial_set
day = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,visited,country):
    
    visited[x][y] = True
    q = deque() # 조건에 만족하는 연합들이 담길 q
    q.append((x,y))

    people_sum = country[x][y]
    area_sum = 1
    areas = [(x,y)]

    while q:
        cx, cy = q.popleft() # 현재 위치좌표

        for i in range(4):
            nx = cx + dx[i] # 다음 위치 좌표
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]: # 만일 벗어나지 않고, 아직 방문하지 않은 나라면
                if L <= abs(country[cx][cy]-country[nx][ny]) <= R: # 그리고 차이가 L과 R 사이면
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    people_sum += country[nx][ny]
                    area_sum += 1
                    areas.append((nx,ny))

    return people_sum, area_sum, areas


while True: # 2000
    visited = [[0]*N for _ in range(N)] # N²
    flag = 0
    for i in range(N): # N³
        for j in range(i % 2, N, 2):
            if not visited[i][j]:
                p,a,ar = bfs(i,j, visited, country)
                if a >= 2:
                    flag = 1
                for x,y in ar:
                    country[x][y] = p//a
    if not flag:
        break
    day+=1

print(day)