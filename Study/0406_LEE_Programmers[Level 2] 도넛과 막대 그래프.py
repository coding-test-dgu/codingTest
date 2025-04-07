from collections import defaultdict
def solution(edges):
    answer = [0, 0, 0, 0] # 정점, 도넛, 막대, 8자
    graph = defaultdict(lambda : [0, 0]) # out_edge, in_edge
    # 반복문 돌면서, 각 노드에 out과 in을 저장
    # [key : node , value : [out, in]]
    for out_edge, in_edge in edges:
        graph[out_edge][0] += 1
        graph[in_edge][1] += 1
    
    for node in graph:
        # 생성 노드
        if graph[node][0] >= 2 and graph[node][1] == 0:
            answer[0] = node
        # 막대 그래프
        if graph[node][0] == 0:
            answer[2] +=1
        # 8자 그래프
        if graph[node][0] ==  2:
            if graph[node][1] > 0:
                answer[3] +=1
    # 도넛 그래프 = 전체 그래프의 개수(생성노드 out_edge) - 막대 - 8자
    answer[1] =  graph[answer[0]][0] - (sum(answer) - answer[0])

    
    # 일단 들어오는 간선이 없고, 나가는 간선이 2 이상 -> 정점임. (ok)
    # 노드 중에 나가는 간선이 2개, 들어오는 간선이 0이 아닐때-> 8자 그래프
    # 노드 중에 나가는 간선 없고 들어오는거 1개인 노드 => 막대 그래프 output 0 input 1 -> bargraph +=1 (ok)
    
    return answer