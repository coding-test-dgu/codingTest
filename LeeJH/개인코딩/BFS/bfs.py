from collections import deque

#bfs는 큐를 이용한 너비 우선 탐색 알고리즘이다.
def bfs(graph, start, visited):
    #큐 구현을 위해 deque라이브러리를 사용한다.
    queue = deque([start])
    #현재 노드를 방문처리
    visited[start] = True
    #큐가 빌때까지 밥ㄴ복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph= [
    [], #0번째 Index
    [2,3,8], #1번 Index와 인접한 노드
    [1,7], #2번 Index와 인접한노드
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
bfs(graph, 1, visited)

#결과 : 1 2 3 8 7 4 5 6