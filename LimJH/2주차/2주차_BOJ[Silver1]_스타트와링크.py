import sys

N = int(sys.stdin.readline()) # 그냥 sys.maxsize해서 sys사용하는 김에 사용함
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N # True: 스타트팀  /  False: 링크팀
ability_gap = sys.maxsize #능력치 차이 최소값 저장

def dfs(cur_start_team_cnt, idx): #(현재까지 고른 스타트 팀원의 수, 다음 선택 시작 위치(중복 없는 순열을 만들기 위해)
    global ability_gap

    # 스타트와 링크 팀이 반반으로 모두 나뉘었다면
    if cur_start_team_cnt == N//2 :

        team_start = 0
        team_link = 0

        # 방문팀(Start)과 미방문팀(Link)팀의 능력치 계산
        for i in range(N):
            for j in range(N):

                # i!=j는 어차피 0이기도 하고 논리적으로 연산에서 빠져야됨
                if i!=j:

                    # 방문팀(Start)의 능력치 합산
                    if visited[i] and visited[j]:
                        team_start += board[i][j]
                    # 미방문팀(Link)의 능력치 합산
                    if not visited[i] and not visited[j]:
                        team_link += board[i][j]

        # 능력치 Gap을 global 변수 ability_gap에 업데이트
        ability_gap = min(ability_gap, abs(team_start - team_link))
    # 아직 절반으로 팀이 나뉘지 않았다면 => 팀 뽑는 과정 진행
    else:
        for i in range(idx, N):
            # 이 부분에서 백트래킹 DFS로 팀이 구성될 모든 조합을 진행
            if not visited[i]:
                visited[i] = True
                dfs(cur_start_team_cnt+1, i+1)
                visited[i] = False

dfs(0,0)
print(ability_gap)