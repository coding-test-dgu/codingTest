import sys
sys.setrecursionlimit(10**6)

initial_set, *country = [list(map(int, line.split()))for line in sys.stdin.readlines()]
N, L, R = initial_set
day = 0
people_sum, area_sum, areas = 0, 0, []


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,visited,country):
    global N, L, R, people_sum, area_sum, areas

    visited[x][y] = True # 현 노드를 방문으로 바꿈
    people_sum += country[x][y]
    area_sum += 1
    areas.append((x,y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]: # 방문되지 않은 노드를 탐색하기 위한 코드, 시발 이거 visited라고 했다.
            if L <= abs(country[x][y] - country[nx][ny]) <= R:
                dfs(nx,ny,visited,country)

while True:
    visited = [[0]*N for _ in range(N)] # 방문 여부 visited, 매일마다 초기화
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 이 노드를 while에서 돌릴지 말지 판단하는 코드
                dfs(i,j, visited, country)
                if flag == 0 and area_sum >= 2:
                    flag = 1
                for x,y in areas:
                    country[x][y] = people_sum // area_sum
            # print(people_sum, area_sum, areas)
            people_sum, area_sum, areas = 0,0,[]
    
    if not flag:
        break
    day += 1

print(day)
                