'''
[Note]
- answer = 최소 사각지대의 개수
   (즉, Office의 0개수가 최소인 상태)
- 모든 cctv가 바라보는 조합의 경우의수 다 보아야하네

[90도 회전 경우의 수]
1번 = 3번회전
2번 = 1번회전
3번 = 3번회전
4번 = 3번회전
5번 = 무회전
'''
N, M = map(int, input().split()) # 최대 8
office = [list(map(int, input().split())) for _ in range(N)]

answer = N*M
#초기 사각 지대 계산
for i in range(N):
    for j in range(M):
        if office[i][j] != 0:
            answer -= 1

# CCTV 위치 파악
cctv_pos = [] # [ (x, y, cctv 번호) ,  ... , ... ]
for i in range(N):
    for j in range(M):
        if 1<=office[i][j]<=5:
            cctv_pos.append((i,j,office[i][j]))

# i CCTV의 방향 정의
'''
    1
2       0
    3
'''
directions = {
    1 : [[0], [1], [2], [3]],
    2 : [[2,0], [1,3]],
    3 : [[0,1], [1,2], [2,3], [3,0]],
    4 : [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5 : [[0,1,2,3]]
}

'''
[현재 가진 정보]
N, M : 사무실 크기 NxM
office : 사무실 정보
cctv_pos : cctv위치
answer : 초기 사각지대 개수
directions : 각 cctv의 가능 방향

[더 있어야 할 모듈]
- 사각지대 계산 함수 (office의 0개수 계산) = chk_zero()
- cctv 회전 함수 (dfs할 때, for d in 4: 이런 것 처럼)
- 탐색할 def함수 (w/ 백트래킹) 
'''
def chk_zero(office_copy):
    zero_cnt = 0
    for i in range(office_copy):
        for j in range(office_copy[0]):
            if office_copy[i][j] == 0:
                zero_cnt+=1
    return zero_cnt
def dfs(level, office):
    global answer # 사각지대 최솟값

    # 모든 CCTV 탐색 완료
    if level == len(cctv_pos):
        answer = chk_zero(office_copy)
        return











