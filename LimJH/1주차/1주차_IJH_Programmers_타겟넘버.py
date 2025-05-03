'''
[IDEA]
-1과 1만을 가진 이진트리 형태로 만들어 DFS알고리즘으로 탐색하도록한다.
이 때, 원하는 숫자 target이 나오면 그것을 반환!
'''
def dfs(v, numbers, depth, target):
    global answer  # answer는 수정까지 할 것이므로 함수에도 global선언
    if depth == N:  # numbers에 있는거 모두 연산 했으면
        if v == target:  # 그 결과가 target과 같은지 확인
            answer += 1  # 같다면 경우의 수 하나 증가
            return
        return

    dfs(v + numbers[depth], numbers, depth + 1, target)
    dfs(v - numbers[depth], numbers, depth + 1, target)


def solution(numbers, target):
    global N, answer
    answer = 0

    N = len(numbers)
    dfs(0, numbers, 0, target)

    return answer

##########################################################[파이써닉한 또 다른 방법]##########################################################
from itertools import product
def solution_v2(numbers, target):
    plus_minus_list = [(x,-x) for x in numbers]
    all_case = list(map(sum, product(*plus_minus_list)))
    return all_case.count(target)

'''
[list(product(*plus_minus_list)) 결과]
[(4, 1, 2, 1), (4, 1, 2, -1), (4, 1, -2, 1), (4, 1, -2, -1), (4, -1, 2, 1), (4, -1, 2, -1), (4, -1, -2, 1), (4, -1, -2, -1), (-4, 1, 2, 1), (-4, 1, 2, -1), (-4, 1, -2, 1), (-4, 1, -2, -1), (-4, -1, 2, 1), (-4, -1, 2, -1), (-4, -1, -2, 1), (-4, -1, -2, -1)]

[map함수로 sum 결과를 반환하도록 한 것이 all_case]
[8, 6, 4, 2, 6, 4, 2, 0, 0, -2, -4, -6, -2, -4, -6, -8]
'''