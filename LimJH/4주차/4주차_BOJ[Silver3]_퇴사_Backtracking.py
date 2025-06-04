# 퇴사 말고 입사..
'''
[인지적 단계]
DFS백트래킹으로 모든 경우의 수를 시도 해보면서, 최소 경우 해를 얻을 수 있을 것이다.
백트래킹은 DFS와 재귀함수를 통해 구현된다. 우선 백트래킹으로 구현해보자.
※언어에 종속되지 않도록 컴프리헨션 문법 지양해보자.
=> 백트래킹으로 아주 잘 풀린다! (만약 시간 초과가 났다면, DP로 해결하면 됐음)

[풀이 설명]
**백트래킹**
그냥 해당 날짜를 선택 or 미선택 이진 트리형태로 탐색한다.
상하좌우 식으로 이동하는게 아니니까 방문처리를 필요없다.
'''
import sys

# init input
N = int(sys.stdin.readline())
schedules = [] # [(T, P), ...]
for day in range(N):
    T, P = map(int, sys.stdin.readline().split())
    schedules.append((T, P))

answer = 0

def dfs(cur_day, cur_profit):
    global answer

    # 종료조건 (재귀함수니까 종료조건 반드시 있어야함)
    if cur_day == N:
        answer = max(answer, cur_profit)
        return

    dfs(cur_day + 1, cur_profit) # 해당 날짜 미선택 (날짜만 증가시킴)
    if cur_day + schedules[cur_day][0] <= N: # 해당 날짜 선택 (cur_profit도 증가시킴)
        dfs(cur_day + schedules[cur_day][0], cur_profit + schedules[cur_day][1])


dfs(0,0)
print(answer)


