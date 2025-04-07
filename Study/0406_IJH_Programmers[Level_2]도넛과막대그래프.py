from collections import defaultdict

'''
[그래프 특징 정리]
- 도넛
끝까지 가면 start_node로 돌아옴
제자리로 오면 모든 그래프 다 탐색완료임

- 막대
끝까지 가도 제자리로 안돌아옴

- 8자
끝까지 가면 start_node로 돌아옴
제자리로 와도 미탐색 노드 존재
'''

# type const.
DONUT = 1
BAR = 2
EIGHT = 3


# 간선과 노드 개수로 판단하는 법
def decision_type_v2(graph, start, cnt_edge, cnt_node, visited):
    global DONUT, BAR, EIGHT

    if cnt_edge == cnt_node:
        print("D")
        return DONUT
    if 2 * cnt_node + 2 == cnt_edge:
        print("E")
        return EIGHT
    if cnt_edge == cnt_node:
        print("B")
        return BAR

    if start not in visited:
        visited.append(start)
        cnt_node += 1
        for nn in graph[start]:
            if nn not in visited:
                cnt_edge += 1
                decision_type_v2(graph, nn, cnt_edge, cnt_node, visited)


# 지금생각해보니 문제에서 나온 내용으로 간단히 처리할 수 있을 거 같음
def decision_type(graph, start, visited):  # DFS O(N+E)
    global DONUT, BAR, EIGHT

    # 첫 방문일 경우 방문
    if start not in visited:
        visited.append(start)  # 방문처리
        print(f'visited / start : {visited, start}')
        print(f'탐색 후보 : {graph[start]}')
        for nn in graph[start]:

            # 인접 노드중 미방문 노드 탐색
            if nn not in visited:
                decision_type(graph, nn, visited)

            # 재방문 노드는 도넛 or 8자
            else:
                print(f'[재방문] : {nn}')
                # 재방문(초기노드로) 했음에도 다음 미방문 노드 존재 => 8자
                for nn in graph[nn]:
                    if nn not in visited:
                        return EIGHT
                # 재방문했고, 다음 미방문 노드 존재X => 도넛
                return DONUT


def solution(edges):
    answer = [0, 0, 0, 0]

    # Adjacent list로 초기화
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
    print(graph)

    # [가정1]에 의해서 생성 노드 결정
    temp = -999
    gen_node = -999
    for key, values in graph.items():
        if temp < len(values):
            temp = max(temp, len(values))
            gen_node = key
    answer[0] = gen_node
    # 생성 노드를 가 가진 인접 노드들이 Starting point
    start_list = graph[gen_node]

    # # start_list 요소를 각각 '독립적으로' 그래프 판단 수행
    # for start in start_list:
    #     visited = []  # 방문한 노드의 숫자를 넣어서 / 중복: 제자리 / 미중복: 미방문 (해당 그래프의 사이즈를 모르므로 이렇게 진행)
    #     idx = decision_type(graph, start, visited)
    #     answer[idx] += 1


    for start in start_list:
        cnt_edge, cnt_node = 0, 0
        visited = []
        answer[decision_type_v2(graph,start, cnt_edge, cnt_node, visited)] += 1

    return answer

'''


가정1: 단방향
간선
개수가
가장
많은
정점이
시작
노드

1 -> 1
2 -> 3, 1
3 ->
4 -> 3
---

1 -> 12
2 ->
3 -> 5, 8
4 -> 11, 2, 8
5 -> 3
6 -> 10
7 -> 11
8 -> 3
9 -> 6
10 -> 11
11 -> 1, 9
12 -> 7

가정1: 단방향
간선
개수가
가장
많은
정점이
시작
노드

'''