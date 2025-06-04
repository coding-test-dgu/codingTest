'''
[문제 이해]
1 2 4 8 9 이고 출력(가장 인접하 공유기 최소거리가 최대가된 값)이 3이다.
1 먼저 설치
1-3 = 2 => 설치 불가
1-4 = 3 => 설치
4-8 = 4 => 설치
8-9 = 1 => 설치 불가
최종적으로 1 4 8이라는 역추적을 해볼 수 있었음

정답의 범위는 10억.
브루트포스는 10억 당 집의 개수를 다 돌아야하니까 => 10억*20만 = 1억을 훨씬 넘어감 => time out
이분탐색을 logN을통해서 10억~=30
(2^10 ~= 1000 / 2^20 ~= 1,000,000 / 2^30 ~= 1,000,000,000 으로 좁혀주자)

ㅇ
(1) 2 _ 4 _ _ _ 8 9 : 1설치
(1) 2 _ 4 _ _ _ 8 9 :
'''

N, C = map(int,input().split()) # max(N) = 200,000 / max(C) = N
routers = sorted([int(input()) for _ in range(N)]) # 집의 좌표들( 최대 10억 )

# [1: 공유기를 설치할 1st집] [r[-1] - r[0] : 공유기를 설치할 last 집]
start, end = 1, routers[-1] - routers[0]
answer = 0
def binary_search(routers, start, end):
    global answer

    while start<=end:
        mid = (start + end) // 2 # 공유기 간 최소 거리를 mid로 가정
        cur_home = routers[0] # 첫 집에 공유기설치
        cnt = 1 # 설치한 공유기 개수

        # 다음 공유기 설치 가능한 집 찾기
        for i in range(1,len(routers)):
            # 현재 집이 이전에 설치된 공유기 위치에서 mid 이상 떨어져 있으면 설치 가능
            if routers[i] >= cur_home + mid:
                cnt += 1 # 공유기 설치
                cur_home = routers[i] # 현재 공유기 위치를 갱신

        # 공유기를 C 이상 설치할 수 있으면 → 더 넓은 간격으로도 설치 가능할 수 있음
        if cnt >= C:
            answer = mid # 현재 mid 거리도 가능한 값이므로, answer에 저장
            start = mid + 1 # 더 큰 거리로도 가능한지 확인하기 위해 오른쪽 탐색
        else:
            end = mid - 1 # 공유기 수 부족 → 간격 좁혀야 하므로 왼쪽 탐색

binary_search(routers, start, end)

print(answer)