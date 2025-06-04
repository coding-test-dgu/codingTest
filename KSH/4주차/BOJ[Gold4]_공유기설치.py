'''

풀이 접근 방식
1. 이분탐색을 하고자하는 대상이 뭐지?
-> 공유기 사이의 최소 거리의 최댓값
2. 공유기를 설치할 집을 골라볼까?
-> 이러면 브루트포스가 되고, 이분 탐색을 사용 안함.
3. 이분 탐색을 사용하는 방법을 모르겠음
-> 못풀고 블로그 보고 공부해서 풀었음.


TODO: 아래 궁금증에 대한 답변 하기.
Q1. 왜 시작과 끝을 공유기 사이의 거리 최댓값으로 하는지
A1. 내가 구하고자 하는게 최대 거리기 때문에, 그 거리의 최소와 최대가 양 끝이 되야지.

Q2. 어떻게 해야 최대거리 이분 탐색 + 공유기를 설치할 수 있는 집의 갯수 구하기
    이런식으로 나눠서 풀 생각을 할 수 있는지
A2. 내가 구하고자 하는 값(대상)을 이분 탐색하면서, 대상의 값이 이럴 때~~~
    문제의 조건을 만족하냐 안하냐를 검증하는 방식으로 푸는 것 같음
 
Q3. 왜 start <= end가 종료 조건인지
A3. start = end 여도 조건 검사를 해도 되기 때문

Q4. 최소거리의 최대를 구하는 이 문제는 어떻게 대처해야하는지
A4. 최소 거리의 최대를 직접 구하려고 할 이유가 없음. 왜 자꾸 안되는 것을 하려고 함.
    이 두개의 조건을 나눠서 사용하려고 하면 됨.
    1. 거리의 최대를 구해야되네. 그럼 거리를 구하고자하는 값으로 선정하자.
    2. 근데 그 거리가 최소인 경우네. 그럼 그 최소인 경우를 가지고 문제의 조건을 구성하자.
        -> 공유기 사이의 거리가 최소이상일 때를 만족하는 공유기 설치 가능 경우를 이용해보자.


'''

import sys

houses, wifi = map(int, sys.stdin.readline().split()) # 집 갯수와 설치해야하는 공유기 갯수
house_location = [] # 집 좌표
for _ in range(houses):
    house_location.append(int(sys.stdin.readline()))

house_location.sort() # 집 좌표 정렬

start = 0 # 공유기 사이 거리 최소 
end = house_location[-1] # 공유기 사이 거리 최대

while start <= end:
    mid = (start + end) // 2 # 공유기 사이 거리를 mid
    cnt = 1 # 설치한 공유기 갯수, 맨 처음에 공유기 설치한다고 가정
    now_location = house_location[0]

    for i in range(1, len(house_location)): # 두번째 집부터 탐색
        if house_location[i] >= mid + now_location:
            cnt += 1
            now_location = house_location[i]

    if cnt >= wifi: # 설치할 수 있는 집 갯수가 같거나 많으면
        start = mid + 1
    else: # 설치할 수 있는 집 갯수가 적으면
        end = mid - 1

print(end)