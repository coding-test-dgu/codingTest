'''
<배운점>
- 함수를 여러개 작성하는 것을 두려워말기


'''


from itertools import combinations
import sys

info, *map = [list(map(int, line.split())) for line in sys.stdin.readlines()]
n, m = info

# 치킨집 좌표 구하는 함수
def chicken_house(map):
    ch_cords = []
    for i in range(n): # 최대 2500
        for j in range(n):
            if map[i][j] == 2:
                ch_cords.append((i,j))

    return ch_cords

# 집 좌표 구하는 함수
def house_cords(map):
    houses = []
    for i in range(n): # 최대 2500
        for j in range(n):
            if map[i][j] == 1:
                houses.append((i,j))
    
    return houses

houses = house_cords(map) # 집 좌표 모음
chicken_houses = chicken_house(map) # 치킨집 좌표들

cases = list(combinations(chicken_houses, m)) # 치킨집 선택하는 경우의 수

min_list = []

# 최대 총 120만
for case in cases: # 최대 13C6 = 1716
    distance_sum = 0 # case에 대한 거리 총합합
    for house in houses: # 최대 100
        min_distance = 99999
        for chicken_house in case: # 6or7
            dx = abs(house[0]-chicken_house[0])
            dy = abs(house[1]-chicken_house[1])
            dL = dx+dy
            if dL < min_distance:
                min_distance = dL
        distance_sum += min_distance
    min_list.append(distance_sum)

print(min(min_list))


#-----------------------------#

# 아래 처럼 치킨집과 집 좌표 동시에 찾게 리팩토링 가능할듯
def find_cords(map):
    ch_cords = [] # 치킨집 좌표
    houses = [] # 집 좌표
    for i in range(n):
        for j in range(n):
            if map[i][j] == 2:
                ch_cords.append((i,j))
            if map[i][j] == 1:
                houses.append((i,j))