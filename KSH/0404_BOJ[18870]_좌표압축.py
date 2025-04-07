# 시간 초과
# 역시 숫자가 크면 수행 시간 큰 것들 겹치면 안됨됨
a, *b = list(map(int, open(0).read().split()))
k = sorted(list(set(b)))

for i in range(0,a):
    b[i] = k.index(b[i])

print(*b, sep=" ")

# 해결
# 딕셔내리로 펼친다는 마인드. 조건 속의 조건X, 딕셔내리로 넓게 펼친다는 생각각
a, *b = list(map(int, open(0).read().split()))
k = sorted(list(set(b)))

mapping = {value:idx for idx, value in enumerate(k)}

b = [mapping[v] for v in b]

print(*b, sep=" ")