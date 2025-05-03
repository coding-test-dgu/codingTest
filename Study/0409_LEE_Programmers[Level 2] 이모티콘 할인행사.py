from itertools import product

def solution(users, emoticons):
    answer = [0, 0]  # [가입자 수, 이모티콘 판매 수익]
    discount_rate = [10, 20, 30, 40]

    # 이모티콘마다 할인율을 조합하는 모든 경우(중복 순열)
    for case in product(discount_rate, repeat=len(emoticons)):
        plus_join = 0  # 이모티콘 플러스 서비스 가입자 수
        total_price = 0  # 총 이모티콘 판매 수익

        for user in users:
            user_discount, user_limit = user
            user_total = 0  # 해당 유저의 이모티콘 구매 총액

            for i in range(len(emoticons)):
                if case[i] >= user_discount:
                    discounted_price = emoticons[i] * (100 - case[i]) // 100
                    user_total += discounted_price

            if user_total >= user_limit:
                plus_join += 1
            else:
                total_price += user_total

        # 조건 우선순위: 1순위 가입자 수, 2순위 판매 수익
        if plus_join > answer[0] or (plus_join == answer[0] and total_price > answer[1]):
            answer = [plus_join, total_price]

    return answer
