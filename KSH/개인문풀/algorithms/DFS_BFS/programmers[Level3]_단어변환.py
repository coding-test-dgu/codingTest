from collections import deque

answer_list = []
answer = 0

# 풀이 1 : answer와 answer_list global
def dfs(current, target, words, visited):
    global answer, answer_list
    
    if current == target:
        answer_list.append(answer)
        return
        
    for i, next_word in enumerate(words):
        diff = 0
        for k in range(len(current)):
            if current[k] != next_word[k]:
                diff += 1
            if diff >= 2:
                break
        if diff == 1 and visited[i] == False:
            visited[i] = True
            answer += 1
            dfs(next_word, target, words, visited)
            # 정답일 때, 
            # 더 이상 못가는 노드일 때 len(set(current)-set(next_word)) >= 2
            # 다 방문한 노드일 때 
            visited[words.index(next_word)] = False
            answer -= 1
    
    return False

# 풀이 2: answer_list만 global
def dfs(current, target, words, visited, count):
    global answer_list
    
    if current == target:
        answer_list.append(count)
        return True
    
    for k, word in enumerate(words):
        diff = 0
        for i in range(len(word)):
            if current[i] != word[i]:
                diff += 1
        if diff == 1 and not visited[k]:
            visited[k] = True
            count += 1
            dfs(word, target, words, visited, count)
            visited[k] = False
            count -= 1
                
    return False

# 풀이 3: bfs로 풀기
answer = []

def bfs(current, target, words):
    global answer
    
    q = deque()
    q.append((current,0))
    
    while q:
        size = len(q)
        for _ in range(size):
            curr = q.popleft()
            if curr[0] == target:
                answer.append(curr[1])
                return
            for k, word in enumerate(words):
                diff = 0
                for i in range(len(word)):
                    if curr[0][i] != word[i]:
                        diff += 1
                if diff == 1:
                    q.append((word,curr[1]+1))

def solution(begin, target, words):
    global answer, answer_list
    
    # for 풀이1,2
    visited = [0]*len(words)
    
    if target not in words:
        return 0 
    
    # 풀이 1
    dfs(begin, target, words, visited)
    # 풀이 2
    dfs(begin, target, words, visited)

    if answer_list == []:
        return 0
    else:
        return min(answer_list)
    
    # 풀이 3
    if target not in words:
        return 0 
    
    bfs(begin, target, words)
    print(answer)
    return min(answer)