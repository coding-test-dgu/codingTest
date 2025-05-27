location = input() # 위치 정보 입력력

row = int(location[1]) # 행 위치
col = int(ord(location[0])) - int(ord('a')) + 1 # 열 위치

moves = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

answer = 0 # 가능한 위치 갯수

for dx, dy in moves:
    print(dx,dy)
    n_row = row + dx
    n_col = col + dy
    if 1<=n_row<=8 and 1<=n_col<=8:
        answer += 1

print(answer)