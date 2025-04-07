from collections import defaultdict


def count_edges(edges):
    OUT_IDX = 0
    IN_IDX = 1
    edge_counts = defaultdict(lambda: [0, 0])

    # edge -> [2,3] : 2의 out1개 / 3의 in 1개
    for v1, v2 in edges:
        edge_counts[v1][OUT_IDX] += 1
        edge_counts[v2][IN_IDX] += 1
    return edge_counts


def check_answer(in_out_cnts):
    ret = [0, 0, 0, 0]
    for key, counts in in_out_cnts.items():  # node : in&out count
        # 생성된 정점의 번호 확인
        if counts[0] >= 2 and counts[1] == 0:
            ret[0] = key

        # 막대 모양 그래프의 수 확인
        if counts[0] == 0 and counts[1] > 0:
            ret[2] += 1

        # 8자 모양 그래프의 수 확인
        if counts[0] >= 2 and counts[1] >= 2:
            ret[3] += 1
    ret[1] = in_out_cnts[ret[0]][0] - sum(ret[1:])

    return ret


def solution(edges):
    answer = []
    in_out_cnts = count_edges(edges)
    answer = check_answer(in_out_cnts)
    return answer