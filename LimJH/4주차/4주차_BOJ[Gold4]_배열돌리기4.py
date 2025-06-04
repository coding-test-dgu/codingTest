import sys
from collections import deque
from itertools import permutations
from copy import deepcopy



# 입력 처리
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
operations = [list(map(int, input().split())) for _ in range(K)]
ans = sys.maxsize


def rotate(arr, r, c, s):
    '''
    :param arr: 회전할 배열
    :param r: 회전 중심 좌표(x)
    :param c: 회전 중심 좌표(y)
    :param s: 회전 범위(s만큼 사각형 크기가 커짐)
    :return: 회전된 결과 배열
    '''

    # STEP1: 회전할 사각형 범위 결정
    for rotate_range in range(1, s+1):
        top = r - rotate_range # 가장 윗 행
        left = c - rotate_range # 가장 왼쪽 열
        bottom = r + rotate_range # 가장 아랫 행
        right = c + rotate_range # 가장 오른쪽 열

        dq = deque()

        # 위쪽 -> 오른쪽으로 진행
        for j in range(left, right):
            dq.append(arr[top][j])

        # 오른쪽 ↓ 아래로 진행
        for i in range(top, bottom):
            dq.append(arr[i][right])

        # 아래쪽 ← 왼쪽으로 진행
        for j in range(right, left, -1):
            dq.append(arr[bottom][j])

        # 왼쪽 ↑ 위로 진행
        for i in range(bottom, top, -1):
            dq.append(arr[i][left])

        dq.rotate(1) # 반시계 1칸 회전

        # 회전한 값 다시 배열에 삽입
        for j in range(left, right):
            arr[top][j] = dq.popleft()
        for i in range(top, bottom):
            arr[i][right] = dq.popleft()
        for j in range(right, left, -1):
            arr[bottom][j] = dq.popleft()
        for i in range(bottom, top, -1):
            arr[i][left] = dq.popleft()

# 모든 연산 순서의 순열 탐색
for perm in permutations(operations, K):
    temp = deepcopy(A)

    for r,c,s in perm:
        rotate(temp, r-1, c-1, s)

    for row in temp:
        ans = min(ans, sum(row))

print(ans)