'''
[Note]
- 숫자카드 개수 = N
- 정수 개수 = M
- answer = 적힌 숫자 카드를 상근이가 몇개 가졌나?

cards 최대 개수는 500,000
targets 최대 개수는 500,000
따라서, 완전탐색으로 풀면 500,000 ** 2 = 250,000,000,000 는 약 250초
'''

from collections import defaultdict
N = int(input())
cards = list(map(int, input().split())) # 이분탐색을 위한 오름차순 정렬
M = int(input())
targets = list(map(int,input().split()))

# 상근이 각 카드의 개수 세기 O(N)
count = defaultdict(int)
for card in cards:
    count[card] += 1

# 상근이 카드에 존재하는 target카드의 개수가 몇개인지 출력
for target in targets: # O(M)
    print(count.get(target, 0), end=" ")

# 결과 시간복잡도 = O(N + M) = 약 1,000,000번 연산량 (1초 내 성공)