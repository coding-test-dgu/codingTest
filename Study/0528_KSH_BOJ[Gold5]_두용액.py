'''

- 투 포인터 두 가지 방식
1. 양쪽에서 좁혀오기
2. 토끼와 거북이

-> 이 문제는 양쪽에서 좁혀오는 유형임
왜? 모든 경우를 살피기 보다, 특정 조건에 가장 가까운 놈을 찾는 거기 때문.

TODO: 투 포인터 알고리즘 공부 심화.

'''

# import sys
#
# n = int(sys.stdin.readline())
# liquids = list(map(int, sys.stdin.readline().split()))
#
# liquids.sort() # 용액 오름차순 정렬
#
# start = 0
# end = 1
# flag = len(liquids) - 1
#
# min_value = 2_000_000_000 # 용액 합의 최소값
# mixed_liq = (0,0) # 최소값을 만드는 용액 두 개개
#
#
# while start < end <= flag:
#
#     mix_value = abs(liquids[start] + liquids[end])
#
#     if mix_value < min_value:
#         min_value = mix_value
#         mixed_liq = (start, end)
#         if end == flag:
#             start += 1
#             end = start + 1
#         else:
#             end += 1
#     else:
#         flag = end - 1
#         start += 1
#         end = start + 1
#
# print(liquids[mixed_liq[0]], liquids[mixed_liq[1]])
'''

           x
[-12 -4 -1 2 8 9 16 18 25 30]
           o o


틀린 부분 1

    if mix_value < min_value and end < len(liquids)-1: # 최솟값 갱신
        min_value = mix_value
        mixed_liq = (start, end)
        end += 1 


'''

import sys

n = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))

liquids.sort() # 용액 오름차순 정렬

start = 0
end = len(liquids)-1

min_value = sys.maxsize # 용액 합의 최소값
mixed_liq = [] # 최소값을 만드는 용액 두 개

while start < end:
    mixture = liquids[start] + liquids[end]
    diff = abs(0-mixture)

    if diff <= min_value: # 0과의 차이가 더 작을 때
        min_value = diff
        mixed_liq = [liquids[start], liquids[end]] # 최소값 만드는 용액들 append
        # mixed_liq.append(liquids[start])
        # mixed_liq.append(liquids[end])
    
    # 양쪽에서 좁혀오는 로직
    if mixture >= 0:
        end -= 1
    else:
        start += 1

print(mixed_liq[0], mixed_liq[1])