'''

풀이 접근 방식
- 백트래킹을 직접 구현하려니 머리 아팠음
-> dfs로 백트래킹을 구현한게 생각나서 이를 이용
- 백트래킹 로직과, 회전 로직을 따로 분리해서 함수를 만들었음
-> 기능을 분리하여 코드를 작성하니, 문제 풀 때 훨씬 편함

아래는 문풀 하면서 남긴 메모...

1. 연산 조합에 따른 case들 나누기
2. 모든 연산을 한번에 할 수도 있고, 백트래킹으로도 할 수 있음.

회전 연산
( r, c, s )
- 각 연산에 대해 s번 만큼 연산이 수행 되야함. s를 1씩 증가하면서 풀면 될듯.
- r, c가 중심 점임.

조합이랑 백트래킹이랑 은근 비슷함

- 이동에 대한 case를 나눠야할 듯.
- 2차원에서 행 슬라이싱 안된다
- max 값 할당하는 스킬

- 백트래킹을 위한 dfs와, 회전을 위한 rotation 함수로 기능을 나눠서
구현하는 것도 방법임. 꼭 한번에 다 구현하려고 할 필요 없다.

- 얕은 복사와 깊은 복사
- 나 rotation은 복구했는데, graph는 안해줌 ㅋㅋ
- 방향 잡을 때 top,bottom, left, right 도 되고, 좌표도 된다.
- r,c로 어렵게 하지말고, top 이런거랑 now, prev, current 이런거를 써
- temp로 원본 그래프를 복사해서 사용해도됨.
    그러면 복잡하게 겹치는 곳 고려 안해도 되지.

- 나 자꾸 사소한 인자실수를 너무 많이함.

'''


import sys

n, m, k = list(map(int, sys.stdin.readline().split()))

graph = [[0] * (m+1) for _ in range(n+1)]
rotate = [] # 회전들을 담을 rotate 배열

for i in range(1, n+1):
    graph[i][1:] = list(map(int, sys.stdin.readline().split())) # 이 부분에서 삽질 오지게 함. 그냥 graph[i]로 해버려서 0열부터 바꾸고 있었음

for i in range(k):
    rotate.append(list(map(int, sys.stdin.readline().split())))

MAX = int(1e18)
minimum = MAX # 모든 경우 중 배열의 최솟값

def rotation(graph, rotate): # 그래프를 회전시킬 rotation 함수
    r,c,s = rotate

    for i in range(1, s+1):
        left_top = graph[r-i][c-i]
        left_bottom = graph[r+i][c-i]
        right_top = graph[r-i][c+i]
        right_bottom = graph[r+i][c+i] # 이 부분도 오지게 삽질함... right_bottom = graph[r-i][c-i]로 함....

        for j in range(1, 2*i+1):
            graph[r-i+j-1][c-i] = graph[r-i+j][c-i]
            graph[r+i-(j-1)][c+i] = graph[r+i-(j)][c+i]
            graph[r+i][c-i+j-1] = graph[r+i][c-i+j]
            graph[r-i][c+i-(j-1)] = graph[r-i][c+i-(j)]

        # 각 꼭짓점 네개의 좌표 모두에 대해 재할당해줘야하는데, 처음에 양쪽 대각 끝만 하다가 계속 틀렸음
        graph[r-i][c-i+1] = left_top
        graph[r+i-1][c-i] = left_bottom
        graph[r-i+1][c+i] = right_top
        graph[r+i][c+i-1] = right_bottom


def dfs(graph, visited): # dfs로 백트래킹 구현하였음.
    global minimum

    if all(visited): # 만약 전부 방문했다면, 최솟값 비교 로직 수행
        graph_min = int(1e18)
        for line in graph[1:]:
            if sum(line[1:]) < graph_min:
                graph_min = sum(line[1:])
        if graph_min < minimum:
            minimum = graph_min

        return

    for i in range(k):
        if not visited[i]:
            visited[i] = True
            origin_graph = [row[:] for row in graph]
            rotation(graph, rotate[i])
            dfs(graph, visited)

            graph = [row[:] for row in origin_graph]

            visited[i] = False


visited = [False] * k
dfs(graph, visited)
print(minimum)

'''
def rotation(graph, rotate): # 로테이션 함수 선언
    global minimum

    if not rotate:
        smallest = int(1e18)
        for p in range(1, n+1):
            if sum(graph[p]) < smallest:
                smallest = sum(graph[p])

        if smallest < minimum:
            minimum = smallest
        return

    for j, case in enumerate(rotate):
        next_rotation = rotate.pop(j)
        r,c,s = case
        for i in range(1,s+1):
            top_left = graph[r-i][c-i] # 왼쪽 맨 위점
            graph[r-i:r+i][c-i] = graph[r-i+1:r+i+1][c-i] # r-i+1 ~ r+i, c-i
            graph[r+i][c-i:c+i] = graph[r+i][c-i+1:c+i+1] # r-i+1 ~ r+i, c-i
            graph[r-i+1:r+i+1][c+i] = graph[r-i:r+i][c+i] # r-i+1 ~ r+i, c-i
            graph[r-i][c-i+1:c+i+1] = graph[r-i][c-i:c+i] # r-i+1 ~ r+i, c-i
            graph[r-i][c-i+1] = top_left
        rotation(graph, next_rotation)

rotation(graph, rotate)
print(minimum)
'''