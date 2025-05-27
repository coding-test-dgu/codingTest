'''
배운 점
1. 시행 때마다 반복적인 작업이 필요할 때, 함수를 선언하자
    - 함수를 여러개 선언하는 것에 두려움 가질 이유 없음
    -> find_shark 같이 아기상어 초기 위치를 찾는 함수를 도입하는 식으로.

2. 항상, 제자리도 방문처리를 해줘야 한다.
    - 안 그러면, 상어의 크기가 9보다 커서, 제자리를 먹어치울 수도 있는 것처럼
        생각하기 까다로울 수 있는 반례를 생각해내야함
    - 일례로, 아기상어가 이동하다가 삼면이 크기가 더 큰 물고기들일 때,
        다시 돌아가야돼서 오류가 나는거에요~ 이러면서 질문게시판에서 사람들이 피드백하고 있었음
        -> 근데, 코테에서 과연 이런거까지 생각을 해야지만이 문제를 풀 수 있게 할까?
        
        물론, 카카오 같은 곳은 이런 창의력/상황판단력 볼거 같음.
        그치만, 기본적인 원리를 적용하는 것이 관건이지, 이런 반례까지 다 쥐어짜내서 생각하면서 코딩할 수 없음.

        물론 이런 반례까지 생각할 줄 알아야하지만, 이것에 집착할 필요는 없고
        문제를 많이 풀면서 하나씩 그냥 챙긴다고 생각하면 됨.

        그리고 심지어 위에서 말한 예시의 피드백은, 굳이 꼭 코드상에 특별한 예외 처리를 해야지 해결되는 것도 아님.
        그냥 bfs 돌리면 알아서 저런 상황도 해결해줌.

        -> 알고리즘의 핵심 작동 원리를 이해하는 것이 중요하다.

    - 결국, "초기 좌표와, 한번 방문한 곳은 방문 처리를 꼭 해준다" 이 기본적인 원리를 잊지않고 적용했으면
        쉽게 풀었을 문제임.

'''



from collections import deque
import sys

N, *graph = [list(map(int, line.split())) for line in sys.stdin.readlines()]

n = N[0]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(current, time, babyShark):

    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((current[0],current[1],time))
    visited[current[0]][current[1]] = True # 상어의 크기가 9보다 커져서, 제자리를 먹어치울 수도 있음...

    can_eat_candidate = [] # 상어가 먹어치울 수 있는 물고기들 리스트

    while q:
        x,y,now_time= q.popleft()
        now_time += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] <= babyShark and not visited[nx][ny]: # 이동가능한 조건
                q.append((nx,ny,now_time))
                visited[nx][ny] = True
                if 0 < graph[nx][ny] < babyShark: # 먹어치울 수 있는 조건
                    can_eat_candidate.append((nx,ny,now_time))

    return can_eat_candidate

# 상어 초기 위치 찾는 함수
def find_shark(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                return (i,j)


babyShark = 2 # 현재 상어 크기
timepass = 0 # 현재 지난 시간간
current = find_shark(graph) # 현재 상어 위치
graph[current[0]][current[1]] = 0 # 현재 상어위치를 0으로 만들어줌줌
eat_count = 0 # 먹어치운 물고기수(for 성장)

while True:

    eatable = bfs(current, timepass, babyShark) # bfs 결과 리스트 할당
    eatable = sorted(eatable, key=lambda x:(x[2],x[0],x[1])) # 결과 리스트 거리순->위쪽->왼쪽 순으로 정렬
    
    if len(eatable) == 0: # 먹을 수 있는 물고기가 없을 때
        print(timepass)
        break
    else:                 # 물고기 먹을 수 있을 때
        target = eatable[0]
        graph[target[0]][target[1]] = 9
        graph[current[0]][current[1]] = 0
        timepass = target[2]
        current = (target[0],target[1])
    
    eat_count += 1
    if eat_count == babyShark: # 상어 성장 가능하다면
        babyShark += 1
        eat_count = 0
