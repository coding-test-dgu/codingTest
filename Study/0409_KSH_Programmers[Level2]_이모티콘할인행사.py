'''
--아이디어--
아 이건 할인율 조합에 대해서 모든 경우를 확인해봐야 겠구나
-> 완전 탐색 해야겠구나

아 근데 뭔가 조건들이 많네?
-> 다중 반복문 써야겠다, 그리고 중첩해도 수행시간이 엄청 크지는 않네

--어려움과 배운점--
너무나도 많은 변수들을 선언하느라 뭐가 뭔지 생각 안남
-> 앞으로는 가독성 있는 변수를 선언해야겠음

다중 반복문 하다보니까 내가 뭐를 반복하는지 기억이 안남
-> 코드 짤 때 주석을 달면서 무엇을 하고 있는지 인자하자

다중 반복 깊어지니까 코드 오류날까봐 무서움
-> 중간중간에 print문으로 디버깅하면서 내가 단계마다 의도한 값이 잘 나오는지 확인하자

문제 똑바로 읽자
-> 할인율 1~40인줄 알고 좌절TV + 등호 조건 안 붙혀서 문제 틀려버림


'''


from itertools import product

def solution(users, emoticons):
    sales = [10,20,30,40]
    
    u_count = len(users)
    e_count = len(emoticons)
    
    max_person = 0
    max_person_list = []
    
    sale_list = list(product(sales, repeat=e_count))
    
    for sale in sale_list:
        person = 0 # 이플 가입자수
        ppp = 0 # 총 구매 비용
        for person_info in users:
            poss = person_info[0] # user 할인율
            price = person_info[1] # user 임티 최대 비용
            price_sum = 0 # 해당 user 임티 구매 비용
            
            i = 0
            while i < e_count: 
                if poss <= sale[i]:
                    price_sum += emoticons[i]*(100-sale[i]) / 100
                i += 1
            
            if price_sum >= price: 
                person += 1
            else:
                ppp += price_sum
        
        if person > max_person:
            max_person = person
            # sale += ppp
            max_person_list = [ppp]
        elif person == max_person:
            # sale += ppp
            max_person_list += [ppp]
        else:
            None
    
    print(max_person_list)

    answer = [max_person, max(max_person_list)]
    
    return answer