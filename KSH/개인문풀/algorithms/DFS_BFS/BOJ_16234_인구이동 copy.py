import sys

initial_set, *land = [list(map(int, line.split()))for line in sys.stdin.readlines()]
N, L, R = initial_set
day = 0

human = 0
lands = 0
cord = []
flag2 = 0

def dfs(x, y, land, visited):
    global N, L, R, day, human, lands, cord, flag2


    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    
    human += land[x][y]
    lands += 1
    cord.append((x,y))

    if lands >= 2:
        flag2 = 1

    if not visited[x][y]: # 방문 안된 노드라면
        visited[x][y] = 1
        
    if x+1 < N and L <= abs(land[x+1][y]-land[x][y]) <= R and not visited[x+1][y]:
        dfs(x+1, y, land, visited)
    elif x-1 > -1 and L <= abs(land[x-1][y]-land[x][y]) <= R and not visited[x-1][y]:
        dfs(x-1, y, land, visited)
    elif y+1 < N and L <= abs(land[x][y+1]-land[x][y]) <= R and not visited[x][y+1]:    
        dfs(x, y+1, land, visited)
    elif y-1 > -1 and L <= abs(land[x][y-1]-land[x][y]) <= R and not visited[x][y-1]:    
        dfs(x, y-1, land, visited)
    for r, c in cord:
        land[r][c] = human // lands

    if flag2 == 1:
        human, lands, cord, flag2 = 0, 0, [], 0
        return True
    else:
        human, lands, cord, flag2 = 0, 0, [], 0
        return False

while True:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            print(i,j)
            a = dfs(i,j,land,visited)
            if flag == 0 and a == True:
                flag = 1
    if not flag:
        break
    day += 1

print(day)