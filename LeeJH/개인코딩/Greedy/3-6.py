# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 작성

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (N==K 로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k # N이 K로 나누어 떨어지지 않을때, 가장 가까운 K로 나누어 떨어지는 수를 찾을 수 있다.
    result += (n - target) # N에서 1을 빼는 연산수를 더해준다.
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result +=(n-1)
print(result)