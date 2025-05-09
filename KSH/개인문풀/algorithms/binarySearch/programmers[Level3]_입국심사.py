def binary_search(times, target, start, end):
    answer = 0
    
    while start <= end:
        mid = (start+end) // 2 # mid라는 시간이 주어졌을 때
        
        total = 0
        
        for time in times:
            total += mid // time # 각 심사관의 심사시간을 주어진 시간으로 나눔
            
        print(mid, total)
        
        if total < target: # 심사인원이 n이 안될때 - 심사시간 부족
            start = mid + 1
        else:                # 심사인원이 n이 넘을 때 - 심시시간 오바
            answer = mid
            end = mid - 1
    
    return answer
    


def solution(n, times): # n: 사람, times: 심사관 심사시간 리스트
    times.sort()
    
    start = 1
    end = times[-1] * n
    print(end)
    
    answer = binary_search(times, n, start, end) # n이 심사될 총 인원
    
    return answer