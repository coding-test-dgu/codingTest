'''

< 회고 >
1. 리스트나 dict에 할당, sort 작업
2. dfs 인자를 달리하며 다양한 풀이
3. dfs 재귀 구현 - return 종료조건과 백트래킹

- global 안쓰고, route로 정답 배열을 인자로 받는 기법
- 어차피 오름차순 정렬할거면 람다 뭐하러 씀. 그냥 sort.
- 백트래킹 기법
    visited와 count 이용하는 경우
    visited 없이 딕셔내리에서 pop과 insert로 처리하는 기법
- 종료조건 : dfs가 return 하는 값?
    무한 재귀를 방지하기 위해 True와 False를 리턴하자.
    return 값과 if~else 조건문을 연동해서 백트래킹 해버림.
- pop(인덱스) 하면 그 인덱스 값 뽑아옴. 매우 좋죠.
    defaultdict에 queue를 받을 수 없어서 list로 이용함

'''

from collections import defaultdict

# 풀이1 : global + 정렬된 ticket 리스트 + visited를 이용한 백트래킹
def dfs(current, sorted_tickets, visited, count):
    global answer
    answer.append(current)
    
    if count == len(sorted_tickets):
        return True
    
    for k, [depart, dest] in enumerate(sorted_tickets):
        if depart == current and visited[k] == False:
            visited[k] = True
            if dfs(dest, sorted_tickets, visited, count+1):
                return True
            visited[k] = False
            
    answer.pop()
    return False

# 풀이1 확장 : 내가 하고 싶었던 거
def dfs(current, sorted_tickets, visited, count):
    global answer
    answer.append(current)
    
    if count == len(sorted_tickets):
        return answer
    
    for k, [depart, dest] in enumerate(sorted_tickets):
        if depart == current and visited[k] == False:
            visited[k] = True
            count += 1
            if dfs(dest, sorted_tickets, visited, count):
                return True
            else:
                visited[k] = False
                count -= 1
                answer.pop()
    return False

# 풀이2 : global + 정렬된 ticket 딕셔내리 + pop과 insert를 이용한 백트래킹
def dfs(current, ticket_dict, count, length):
    global answer
    
    answer.append(current)
    
    if count == length:
        return True
    
    
    for idx, dest in enumerate(ticket_dict[current]):
        ticket_dict[current].pop(idx)
        count += 1
        d = dfs(dest, ticket_dict, count, length)
        
        if d == True:
            return True
        else:
            ticket_dict[current].insert(idx, dest)
            count -= 1
            answer.pop()
            # return False

# 풀이3 : global 안쓰기
def dfs(current, sorted_tickets, visited, count, route):
    global answer
    
    route.append(current)
    
    if count == len(sorted_tickets):
        return route
    
    for k, [depart, dest] in enumerate(sorted_tickets):
        if depart == current and visited[k] == False:
            visited[k] = True
            count += 1
            # route.append(dest) # 여기서 append 할거면, solution 함수에서 route로 ["ICN"] 받아야함함
            if dfs(dest, sorted_tickets, visited, count, route):
                return True
            else:
                visited[k] = False
                count -= 1
                route.pop()
            
    return False


def solution(tickets):
    
    # for 풀이 1 (주석 해제)
    sorted_tickets = sorted(tickets, key=lambda x: (x[0], x[1])) # 티켓 소팅
    
    start = "ICN"
    visited = [False] * len(sorted_tickets)
    count = 0

    dfs(start, sorted_tickets, visited, count)

    # for 풀이 2
    ticket_dict = defaultdict(list)
    
    for depart, dest in tickets:
        ticket_dict[depart].append(dest)
        ticket_dict[depart].sort()
    
    start = "ICN"
    count = 0
    length = len(tickets)
    
    dfs(start, ticket_dict, count, length)

    # for 풀이 3
    sorted_tickets = sorted(tickets, key=lambda x: (x[0], x[1])) # 티켓 소팅
    
    start = "ICN"
    visited = [False] * len(sorted_tickets)
    
    count = 0
    route = []
    
    dfs(start, sorted_tickets, visited, count, route)
    answer = route

    return answer