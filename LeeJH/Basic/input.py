import sys
# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 split해서 입력(정수형 리스트)
data = list(map(int,input().split()))

# n, m, k를 공백기준으로 구분하여 입력(정수형)
n, m, k = map(int, input().split())


#내림차순
data.sort(reverse=True)
print(data)
print(n, m, k)

a_data = sys.stdin.readline().rstrip()
print(a_data)

answer = 7
print("정답은" +" " + str(answer) + "입니다.")
print(f"정답은 {answer}입니다.")