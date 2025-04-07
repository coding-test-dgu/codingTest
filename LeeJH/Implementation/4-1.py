# 상하좌우

# N 입력받기
n = int(input())
x, y = 1, 1 # 초기값 (1,1)
plans = input().split() # 이동 계획 입력력

# L, R, U, D에 따른 이동 방향 벡터!
# L로 이동하면 ex) (2,2) -> (2,1) 로 이동하므로, -1이 된다. 
# 이런 식으로, L, R, U, D에 대한 방향백터를 x와 y의 변화량에 대해서 만든다.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나식 확인한다.
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(moves_types)):
        if plan == moves_types[i]: # L R U D 중 뭐인지 확인한다.
            nx = x + dx[i] # x 이동
            ny = y + dy[i] # y 이동
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

print(x, y)