'''

-- 문풀후기 --
진짜 뒤지게 어렵게도 풀었다.
DFS로 한번에 처리하면 되는 거를 왼쪽진행과 오른쪽 진행을 
나눠서 함수를 선언하느라 머리 빠개짐.

그냥 한번에 dfs로 선언하고, 재귀적 호출속에서 받는 인자로 더하고 빼는 식으로
변수를 넣어주면 훨 쉽게 풀 수 있음

'''

#---------------------------#

answer = 0 # 정답 개수 변수 선언언

# 더하는 경우에 이진트리의 왼쪽 자식 노드로 이동하는 함수
def dL(numbers, target, x, idx):
    global answer
    x += numbers[idx]   # 현재 값에 numbers의 다음 값을 더함
    idx += 1            # 인덱스 1 증가
    
    if len(numbers) == idx: # 만일 numbers의 원소들을 다 더하거나 뺐으면
        if x == target:     # 타게트 값과 같으면
            answer += 1     # 정답 갯수 증가
        return None
    dL(numbers, target, x, idx) # 더하는 경우의 재귀적 호출
    dR(numbers, target, x, idx) # 빼는 경우의 재귀적 호출


# 뺴지는 경우에 이진트리의 오른쪽 자식 노드로 이동하는 함수
def dR(numbers, target, x, idx):
    global answer
    x -= numbers[idx]
    idx += 1
    
    if len(numbers) == idx:
        if x == target:
            answer += 1
        return None
    
    dL(numbers, target, x, idx) 
    dR(numbers, target, x, idx) 
    
def solution(numbers, target):
    idx = 0 # 현재 인덱스
    dL(numbers, target, 0, idx) 
    dR(numbers, target, 0, idx)
    
    return answer