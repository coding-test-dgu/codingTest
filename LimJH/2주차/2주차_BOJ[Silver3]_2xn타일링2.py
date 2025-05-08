import sys

'''
f(n) : 가능한 타일 수
f(1) ; 2x1직사각형 = 1개
f(2) ; 2x2직사각형 = (세로2줄, 가로2줄, 통) 3개
f(3) ; 2x3직사각형 = (세로3줄, 세로1개 가로2개, 가로2개 세로 1개, 세로1개 통1개, 통 1개 세로1개) 5
대충 f(n) = f(n-2)*2 + f(n-1) 이겠지. 근데 직접 그려서 확인했는데 머리 약간 아프네
'''
N = int(sys.stdin.readline())
DIVISOR = 10_007
dp = [0] * 1001 # 1<= N <= 1,000
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = 2*dp[i-2] + dp[i-1]

print(dp[N]%DIVISOR)