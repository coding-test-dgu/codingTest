# 1순위 플러스 가입자 수
# 2순위 총 판매액
from itertools import product


def solution(users, emoticons):
    answer = [0, 0]  # [플러스 가입자, 매출액]
    N = len(users)  # 카카오톡 사용자 수
    M = len(emoticons)  # 이모티콘 수
    discounts = [10, 20, 30, 40]  # 가능한 할인율 (one of discounts)

    # print(N, M)
    # print(f'users : {users}')
    # print(f'emoticons : {emoticons}')
    all_discount_case = list(product(discounts, repeat=M))  # 가능한 상품 할인의 모든 조합 경우의 수 (m은 최대 7....4**7 = 16,384)
    # print(f'all_discount_case : {list(all_discount_case)}\n')

    # 모든 할인 조합에 대해서 진행 (..) , (..), (..), ... , (..)
    for discount_case in all_discount_case:  # O(16840)
        total_subscribe_cnt = 0  # 현 조합에 대한 플러스 가입자
        total_price = 0  # 현 조합에 대한 총 매출액

        # 특정 할인 조합 경우에 대한 사용자들 for (10,10,10,20)
        for user_rate, user_limit_price in users:  # O(N) 100
            price = 0

            # 특정 사용자가 특정 할인 조합에 대해서 구매 action진행(각 이모티콘에 대하여 action)
            for emoticon_idx in range(M):
                emoticon_discount_rate = discount_case[emoticon_idx]  # idx번째 상품의 현재 할인율
                if emoticon_discount_rate >= user_rate:  # 이모티콘 할인율이 내 기준보다 높으면
                    price += emoticons[emoticon_idx] * (1 - emoticon_discount_rate / 100)  # 그 이모티콘 구매

            # 특정 사용자가 구매를 다 완료하면, 기준 총가격 넘었는지 확인해야함
            if price >= user_limit_price:  # 총가격 기준치 넘었으면
                total_subscribe_cnt += 1  # (현 할인율 조합에 대한) 구독자 1명 추가
                # subscribe_flag = True
            else:  # 매출액만 추가
                total_price += price

        # 모든 유저에 대해서 끝났으면, 어떤 조합이 가장 좋았는지 평가해야함
        # 먼저 가입자 수가 더 많도록 비교
        if total_subscribe_cnt > answer[0]:  # 플러스 구독자가 더 많은 조합이었다면 업데이트
            answer[0] = total_subscribe_cnt
            answer[1] = total_price
        elif total_subscribe_cnt == answer[0]:
            answer[1] = max(answer[1], total_price)

    return answer