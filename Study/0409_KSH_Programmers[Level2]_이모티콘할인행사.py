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