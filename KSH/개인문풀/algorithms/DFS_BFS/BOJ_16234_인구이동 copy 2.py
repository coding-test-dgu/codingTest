import sys

sys.setrecursionlimit(10**6)

initial_set, *country = [list(map(int, line.split()))for line in sys.stdin.readlines()]
N, L, R = initial_set
day = 0
count_human, count_country, countries = 0,1,[]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,country,visited):
    global N,L,R, day, count_human, count_country, countries

    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    
    if not visited:
        visited[x][y] = True

        for i in range(4): # 미쳤나봐 왜 처음에 i가 아니라 _로 했냐?
            ax = x + dx[i]
            ay = y + dy[i]
            a = dfs(ax,ay,country,visited)
            if a and L <= abs(a-country[x][y]) <= R:
                count_human += a
                count_country += 1
                countries.append((ax,ay))

    return country[x][y]



while True:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 이거 추가하니까 수행시간 기하급수적으로 빨라짐짐
                count_human += country[i][j]
                countries.append((i,j))
                dfs(i,j,country,visited)
                if flag == 0 and count_country >= 2:
                    flag = 1
                for x,y in countries:
                    country[x][y] = count_human//count_country
                
                count_human, count_country, countries = 0,1,[]

    if not flag:
        break
    day += 1

print(day)