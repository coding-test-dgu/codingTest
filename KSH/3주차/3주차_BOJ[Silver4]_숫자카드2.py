'''
<배운점>
풀이 1.
- bisect left, right 할 때, 찾을 값이 존재하지 않으면,
    left와 right값이 같음.
- left는 그 값의 시작 인덱스, right는 끝나는 인덱스 + 1을 돌려줌.

풀이 2.
- 숫자 50만개라서, 해시테이블 해도 된다.

'''

# 풀이 1. 이진탐색 이용
from bisect import bisect_left, bisect_right
import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
find_list = list(map(int, sys.stdin.readline().split()))

num_list = sorted(num_list)

for find_num in find_list:
    left_idx = bisect_left(num_list, find_num)
    right_idx = bisect_right(num_list, find_num)

    if left_idx == right_idx:
        print(0, end=" ")
    else:
        print(right_idx-left_idx, end=" ")

# 풀이 2. 해시테이블 이용
from collections import defaultdict
import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
find_list = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(int)

for number in num_list:
    dic[number] += 1

for find_num in find_list:
    print(dic[find_num], end=" ")