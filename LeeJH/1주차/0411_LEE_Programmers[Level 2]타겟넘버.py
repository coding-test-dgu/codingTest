from collections import deque

#bfs로 풀어봄
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0)) #(total, idx)
    
    while queue:
        total, idx = queue.popleft()
        # idx가 numbers의 길이와 동일? => 모든 숫자를 다 사용한 것.
        if idx == len(numbers):
            # 그때, 합한 total이 target과 같다면, answer(+1)
            if total == target:
                answer += 1
        # 해당 idx의 number를 더하거나 뺀값을, total에 넣고 큐에 append
        else:
            queue.append((total + numbers[idx], idx + 1))
            queue.append((total - numbers[idx], idx + 1))
        
    return answer