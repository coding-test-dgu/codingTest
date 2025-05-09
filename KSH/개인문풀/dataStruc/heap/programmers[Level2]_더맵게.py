import heapq

def solution(scoville, K):
    
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) == 1:
            return -1
        
        small_1st = heapq.heappop(scoville) # 가장 작은 음식 뽑기
        small_2nd = heapq.heappop(scoville) # 두번째로 작은 음식 뽑기
        
        if small_1st >= K and small_2nd >= K:
            break
            
        mixed = small_1st + (small_2nd * 2)
        
        heapq.heappush(scoville, mixed)
        
        answer += 1
    
    return answer