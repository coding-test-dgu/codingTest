from itertools import combinations

def solution(clothes):
    clothing = {} # 옷을 종류에 따라 담을 dict
    
    for clothe in clothes:
        if clothing.get(clothe[1]) == None:
            clothing[clothe[1]] = [clothe[0]]
        else:
            clothing[clothe[1]].append(clothe[0])
    print(clothing)
    

    k = len(clothing) # 조합을 쓰기 위해 key 갯수 할당
    print(k)
    count = 0 # 옷 조합 가짓수 변수
    
    c_count = []
    for key in clothing.keys():
        ccc = clothing[key]
        print(ccc, len(ccc))
        c_count.append(len(ccc))
        
        # c_count.append(len(dict[key]))
    
    # for i in range(1,k+1):
    #     result = list(combinations(c_count,i))
        
    
    
    answer = 0
    return answer