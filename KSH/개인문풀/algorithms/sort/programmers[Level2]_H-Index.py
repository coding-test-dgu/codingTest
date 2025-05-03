def solution(citations):
    
    c = citations
    c.sort(reverse=True)
    
    h_index = 0
    k = len(c)
    
    while k>-1:
        if k <= c[k-1]:
            h_index = k
            break
        k -= 1
    
    return h_index