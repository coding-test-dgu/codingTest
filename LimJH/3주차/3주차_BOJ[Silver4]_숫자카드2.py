'''
[Note]
- 숫자카드 개수 = N
- 정수 개수 = M
- answer = 적힌 숫자 카드를 상근이가 몇개 가졌나?

cards 최대 개수는 500,000
targets 최대 개수는 500,000
따라서, 완전탐색으로 풀면 500,000 ** 2 = 250,000,000,000 는 약 250초

이분탐색은 logN 으로 풀어야함
'''

from collections import defaultdict
N = int(input())
cards = sorted(list(map(int, input().split()))) # 이분탐색을 위한 오름차순 정렬
M = int(input())
targets = list(map(int,input().split()))

# 상근이 각 카드의 개수 세기
count = defaultdict(int)
for card in cards:
    count[card] += 1

def binary_search(start, end, cards, target):
    if start>end:
        return 0

    mid = (start + end) // 2

    if cards[mid] == target:
        return count.get(target)
    if cards[mid] > target:
        return binary_search(start, mid-1, cards, target)
    if cards[mid] < target:
        return binary_search(mid+1, end, cards, target)


for target in targets:
    print(binary_search(0,len(cards)-1, cards, target), end=" ")