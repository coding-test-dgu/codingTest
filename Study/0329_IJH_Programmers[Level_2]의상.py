from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    
    # 각 옷 종류(category)별로 개수를 센다
    for clothe, category in clothes:
        
        dic[category] += 1
        '''
        [*defaultdict 안쓸거면]
        dic[category] = dic.get(category, 0) + 1 로 해도 됨.(get의 2번째 인자가 없을 경우 default값 설정)
        '''
    
    print(f'dic : {dic.items()}')

    # 각 종류마다 (해당 옷을 입는 경우 + 안 입는 경우) → +1
    for v in dic.values():
        print(answer, v+1)
        answer *= (v + 1)

    # 아무것도 안 입는 경우 하나를 제외해야 하므로 -1
    return answer - 1
'''
[추가 설명]
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
음.. 뭐라 설명해야하지 ㅇㅁㄴ ㅇㄴㅁ아ㅣㅁㄴ암ㄴㅇㅁ

#Given
모자 -> 노랑모자, 초록터번?
선글라스 -> 파랑선글라스

#Logic
예를 들어, (A,b) (B,b) (C,c)가 있다면, 모든 경우의수
A B C / AB AC BC / ABC 까지 7가지가 나와야 할 것!
위의 개수는 (1, 1, 1)이다.
1*1*1 (입고, 입고, 입을 확률) = 3
근데 안입는 경우도 생각 해야함
(입거나 안입거나 * 입거나 안입거나 * 입거나 안입거나) = (2 * 2 * 2) = 8
근데 [코니는 하루에 최소 한 개의 의상은 입습니다.]라고 했으니 안입는 경우의 수 하나 빼주기

'''