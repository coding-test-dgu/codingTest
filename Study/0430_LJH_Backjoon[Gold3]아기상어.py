
'''
[아기상어 룰]
- 자신보다 큰 물고기 => 이동불가능
- 작은 물고기 => 먹기 & 이동
- 같은 물고기 = > 이동
- 1칸 이동 시간 = 1초
- 먹은 수 == 자신의 크기  => 크기 1증가

[아기상어 이동 결정 방법]
- 더 이상 먹을 수 있는 물고기 없으면 => 엄마
- 먹을 수 있는 고기 1마리 => 먹으러 가
- 먹을 수 있는 고기 > 1 => 거리 가장 가까운 고기 먹으러 가
    *가장 가까운 거리 = 지나야 하는 칸의 최소 개수
    * 가까운 물고리 여러 마리 => 가장 위(1st),왼쪽(2nd)에 있는 물고기를.

[목표 return]
- 몇 초 동안 엄마 도움 없이 아기가 먹을 수 있는지 구해
'''
from collections import deque


def find_init_baby_loc(board):
    global N
    for x in range(N):
        for y in range(N):
            if board[x][y] == 9:
                return x,y


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
cur_x, cur_y = find_init_baby_loc(board) # (x,y)

#상하좌우(이동방향)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 아기상어 크기
baby_size = 2
def find_eatable_fishs(x, y, baby_size): # with BFS

    visited = [[False]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    q = deque([(x, y)])
    candidates = []

    while q:
        cur_baby_x, cur_baby_y = q.popleft()

        for direction in range(4):
            nx = cur_baby_x + dx[direction]
            ny = cur_baby_y + dy[direction]

            # Grid 밖에 벗어나는지 확인
            if nx>=0 and ny>=0 and nx<N and ny<N:
                # 처음 방문하는 곳인지 확인
                if not visited[nx][ny]:
                    # 이동 가능한지 확인
                    if board[nx][ny] <= baby_size:
                        # 아기 상어가 이동
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        distance[nx][ny] = distance[cur_baby_x][cur_baby_y] + 1
                        # 이동했으면 먹을 수 있는지 확인
                        if board[nx][ny] < baby_size and board[nx][ny] != 0:
                            #eat_candidates에 등록
                            candidates.append((nx,ny,distance[nx][ny]))

    # 가장 가까운게 중요 => 위쪽에 있는게 중요 => 왼쪽에 있는게 중요
    return sorted(candidates, key=lambda x: (x[2], x[0], x[1]))

# BFS(find_eatable_fishs)를 통해 step by step으로 아기상어 사이즈 진화시키기
answer = 0
cnt = 0
while True:
    '''
    candidates를 구하여 다 먹고 다음 round로 가는 것이 아니라,
    1마리만 먹고 난 뒤에, 다음 round로 넘어가야한다.
    '''

    # n번째 Round
    # candidates ; (먹을 고기 x좌표, 먹을 고기 y좌표, 라운드 이동시간)
    candidates = find_eatable_fishs(cur_x, cur_y, baby_size)

    # CASE1)더 이상 먹을게 없으면 종료
    if len(candidates) == 0:
        break

    # CASE2) 아직 먹을 수 있는게 있음
    nx, ny, round_time = candidates[0]

    # 이동 및 먹음 처리
    answer += round_time
    board[nx][ny] = 0
    board[cur_x][cur_y] = 0

    cur_x, cur_y = nx, ny
    cnt += 1

    # 아기상어 크기 증가
    if baby_size == cnt:
        baby_size += 1
        cnt=0

print(answer)




