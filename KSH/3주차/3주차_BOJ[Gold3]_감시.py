'''
1. 문제 후기
2. 접근 방법
2. 배운점, 깨달은 점



이 문제 아직 못풀었는데, 토요일에 좀 더 도전하겠습니다...


changed_office = office
깊은 복사로 바꿈

수학적 기교 - 더 이상 가능성이 없으면 탐색을 stop

아 그니까 너말이 확실한지 다시 검토해봐.
내가 이해한거는, 만약 cctv가 8개로 최대경우고,
cctv 4로 전부 구성 되어있으면 cctv 마다 4번의 case에 대해 3번 좌표를 돌려야하고,
그리고 마지막에 cctv를 전부 다 사용했을 때 또 for 문으로 검사하니까

최악경우 - cctv 4번으로 전부 구성, 8개의 cctv
    (4*3*8)의 8 제곱 * 64


재귀 호출과 연산량과 재귀와 호출의 수행시간의 관계

아 이게 시발 미치겠는게 너가 알려준 chaged로 해도 틀리고,
내가 처음에 했던 얕은 복사도 틀리고,
깊은 복사로 하면 특정 케이스는 수행시간이 초과되고

방법 1: 얕은복사
방법 1: 깊은 복사
방법 1: changed로 해서, 원래 그래프로 돌려주기
방법 1: 모든 그래프를 밖의 ans에 넣어서, if 문 돌려줘서 최솟값 찾기 ( 왜냐면, 재귀 끝단에서 for 중첩으로 세면, 너무 횟수가 많아짐 )
방법 1: 0의 갯수만

수행시간 교훈, for문 밖으로 빼는 교훈,
얕은,깊은 복사 교훈, 내가 왜 하나의 cctv만 하면 되는데 모든 cctv를 재귀마다 했는지
움직일 수 있는 방향 조합을 미리 선언하는 교훈 - 이거를 해시테이블로 하는 교훈,
항상 주석 쓰면서 내가 무슨 작업을 하는지,
백트래킹 교훈
'''


import sys
import copy

info, *office = [list(map(int, line.split())) for line in sys.stdin.readlines()]

n, m = info

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def find_cctv_wall(office):
    cctv_location = []
    wall_location = []
    for i in range(n):
        for j in range(m):
            if office[i][j] in [1,2,3,4,5]:
                cctv_location.append((office[i][j],i,j))
            elif office[i][j] == 6:
                wall_location.append((office[i][j],i,j))
    
    return cctv_location, wall_location

cctv_location, wall_location = find_cctv_wall(office)
cctv_location = sorted(cctv_location, key=lambda x:-x[0])

cctv_pointers = {
    1: [[(1,0)], [(-1,0)], [(0,1)], [(0,-1)]],
    2: [[(0,1), (0,-1)], [(1,0),(-1,0)]],
    3: [[(1,0),(0,-1)],[(1,0),(0,1)],[(-1,0),(0,-1)],[(-1,0),(0,1)]],
    4: [[(1,0),(0,1),(-1,0)], [(0,1),(-1,0),(0,-1)], [(-1,0),(0,-1),(1,0)], [(0,-1),(1,0),(0,1)]],
    5: [[(1,0),(-1,0),(0,1),(0,-1)]]
}

# ans = 999999
ans = []

def office_cases(office, cctv_location):
    global ans

    if not cctv_location:
        # count = 0
        # for i in range(n):
        #     for j in range(m):
        #         if office[i][j] == 0:
        #             count += 1
        # if count < ans:
        #     ans = count
        ans.append(office)
        return "done"

    # for cctv in cctv_location:
    #     cctv_type, x, y = cctv

    cctv_type, x, y = cctv_location[0]

    for case in cctv_pointers[cctv_type]: # cctv 종류에 대한 회전 case에 대해 4
        # changed_office = copy.deepcopy(office) # 64
        changed = []
        for dx,dy in case: # 3
            nx = x+dx
            ny = y+dy # 이동한 좌표 nx, ny
            while 0<=nx<n and 0<=ny<m:    # office 그래프를 벗어나지 않았을 때 8
                if office[nx][ny] == 6:   # 벽이면 stop
                    break
                if office[nx][ny] == 0:
                    office[nx][ny] = 9
                    # changed_office[nx][ny] = 9
                    changed.append((nx,ny))
                nx += dx
                ny += dy
        office_cases(office, cctv_location[1:])
        # office_cases(changed_office, cctv_location[1:])
        for cx, cy in changed:
            office[cx][cy] = 0

    return "done"

office_cases(office, cctv_location)

result = 99

for office_case in ans:
    count = 0
    for i in range(n):
        for j in range(m):
            if office_case[i][j] == 0:
                count += 1
    if count < result:
        result = count

print(result)
