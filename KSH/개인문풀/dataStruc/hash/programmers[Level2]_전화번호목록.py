# 그리디 - 길이로 정렬해서, 짧은 것이 그 이후 긴 것들에 속하는지.
# 만일 하나라도 접두사다? 그럼 루프 멈추고 함수 종료

from collections import defaultdict

def solution(phone_book):
    
    phone_num = defaultdict(list) # 번호의 길이에 따라 번호를 저장할 해시
    for number in phone_book:
        phone_num[len(number)].append(number)
    
    # print(phone_num)
    
    if len(phone_num) == 1:
        return True
    
    num_lengths = sorted(list(phone_num.keys())) # 존재하는 번호 길이들(key)를 정렬한 것
    
    # print(num_lengths)
    for i, key in enumerate(num_lengths):
        numbers = phone_num[key] # 비교할 key의 번호들
        for num in numbers: # key 속의 숫자들에 대해. 숫자들을 하나씩 뽑아옴
            for kkey in num_lengths[i+1:]: # 다른 이후의 모든 키들에 대한 루프
                compare_nums = phone_num[kkey]
                for c in compare_nums:
                    if num in c[:len(num)]:
                        return False
    
    return True
        

    # for key in phone_num.keys(): # 번호의 길이에 따라
    #     for value in phone_num[key]: # 저장된 번호들을 하나씩 뽑아옴
            
    