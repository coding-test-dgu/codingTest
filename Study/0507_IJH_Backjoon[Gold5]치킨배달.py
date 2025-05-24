# 시간제한 1초
# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
# M : 폐업시키지 않을 치킨집의 최대 개수

def find_chicken_coords():
    results = []
    global board, N
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                results.append((i,j))
    return results
def find_house_coords():
    results = []
    global board, N
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                results.append((i,j))
    return results

def back(depth, idx):
    global selected, chicken_coords, house_coords, result

    if depth == M:
        #방문처리된거(폐업대상) / 미방문(개업대상)

        # 도시의 치킨 거리
        city_chicken_dist = 0

        # house는 전부 다 고려
        for h_x, h_y in house_coords: #O(집의 개수 1의 개수)
            min_house_chicken_dist = sys.maxsize
            for i in range(len(chicken_coords)): #O(2의 개수)
                # 선택된 치킨집만 카운트
                if selected[i]:
                    c_x, c_y = chicken_coords[i]
                    min_house_chicken_dist = min(min_house_chicken_dist
                                             ,abs(h_x-c_x) + abs(h_y-c_y))
            city_chicken_dist += min_house_chicken_dist
        result = min(result, city_chicken_dist)

    else: # 폐업 시키지 않을 치킨집 M개 방문처리로 선택 (이 부분을 itertools의 combination을 활용해서 할 수도 있음 조합을 백트래킹으로 대체한 것 뿐임. 그래도 백트래킹에 익숙해지자. Java는 comb없으니)
        for i in range(idx, len(chicken_coords)):
            if not selected[i]:
                selected[i] = True
                back(depth+1, i+1) #✍️TODO: 왜 i+1인지 같이 커밋(중복된 결과를 없애기 위한 것인데 왜 어떻게 없어지는 것인지 잘 이해할 수 있도록)
                selected[i] = False

import sys
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chicken_coords = find_chicken_coords() # 치킨집 좌표
house_coords = find_house_coords() # 집 좌표
selected = [False] * len(chicken_coords)
result = sys.maxsize
back(0,0)
print(result)

'''
🔥TODO: 왜 i+1인지 같이 커밋(중복된 결과를 없애기 위한 것인데 왜 어떻게 없어지는 것인지 잘 이해할 수 있도록)

백트래킹에서 조합을 찾아내는데에 있어서 중복된 것을 만들지 않도록하는 중요한 부분임.

[요약]
i+1을 인자로 넘김으로써 , '이미 선택한 인덱스보다 뒤에 있는 것들만 선택'하도록 제한해서
'중복된 순열은 건너뛰고' 조합만 생성하게 되는 것이다.
'''