'''
이 문제 아직 못풀었는데, 토요일에 좀 더 도전하겠습니다...


'''


import sys

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

ans = 999999

def office_cases(office, cctv_location):

    if not cctv_location:
        count = 0
        for i in range(n):
            for j in range(m):
                if office[i][j] == 0:
                    count += 1
        if count < ans:
            ans = count
        return "done"

    cctv = cctv_location[0]

    if cctv[0] == 5:
        x = cctv[1]
        y = cctv[2]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0<= nx <n and 0<= ny <m: # 이거 True로 하지말고, 조건을 넣는 스킬
                if office[nx][ny] == 6:
                    break
                if office[nx][ny] == 0:
                    office[nx][ny] = 9
                nx = nx + dx[i]
                ny = ny + dy[i]
        office_cases(office, cctv_location[1:])
    elif cctv[0] == 4:
        x = cctv[1]
        y = cctv[2]
        # for i in range(3):
